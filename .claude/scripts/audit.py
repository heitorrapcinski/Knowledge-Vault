#!/usr/bin/env python3
"""
Auditoria de saude do Engineering Knowledge Vault.

Uso, a partir da raiz do repositorio:
    python3 .claude/scripts/audit.py            # vault inteiro
    python3 .claude/scripts/audit.py "02 Permanent Notes/Concepts"

Reporta: total de notas, links quebrados agrupados por origem, notas orfas,
notas sem links de saida, hubs do grafo, conformidade de frontmatter,
valores de type/status fora do vocabulario e taxonomia de tags.

O objetivo nao e zerar os numeros. Link quebrado dentro de um cluster em
construcao declarada e intencional. O que importa e regressao.
"""

import collections
import os
import re
import sys

IGNORE_DIRS = {".git", ".obsidian", ".claude", "node_modules", "_to_delete"}
ROOT_DOCS = {"README", "CLAUDE", "CHANGELOG"}

FM_FIELDS = ["title", "aliases", "tags", "type", "status", "source", "author", "created"]
VALID_TYPE = {"literature", "concept", "practice", "moc", "project"}
VALID_STATUS = {"seed", "growing", "evergreen"}
LEGACY = {
    "permanent-note": "concept",
    "project-case": "project",
    "permanent": "evergreen",
    "moc": "evergreen (status)",
}


def find_notes(base):
    out = []
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        for fn in filenames:
            if fn.endswith(".md"):
                out.append(os.path.join(dirpath, fn))
    return sorted(out)


def parse_list_field(fmraw, key):
    m = re.search(r"^%s:\s*\n((?:[ \t]+-\s.*\n)+)" % key, fmraw, re.M)
    if m:
        return [re.sub(r"^\s*-\s*", "", l).strip().strip("\"'") for l in m.group(1).splitlines()]
    m = re.search(r"^%s:\s*\[(.*)\]\s*$" % key, fmraw, re.M)
    if m:
        return [v.strip().strip("\"'") for v in m.group(1).split(",") if v.strip()]
    m = re.search(r"^%s:\s*(\S.*)$" % key, fmraw, re.M)
    if m:
        return [m.group(1).strip().strip("\"'")]
    return []


def scalar(fmraw, key):
    m = re.search(r"^%s:\s*(\S.*)$" % key, fmraw, re.M)
    return m.group(1).strip().strip("\"'") if m else None


def strip_code(txt):
    """Remove blocos cercados e codigo inline: exemplos nao sao links reais."""
    txt = re.sub(r"^(`{3,})[^\n]*\n.*?^\1[ \t]*$", "", txt, flags=re.S | re.M)
    return re.sub(r"`[^`\n]+`", "", txt)


def load(path):
    txt = open(path, encoding="utf-8").read()
    name = os.path.splitext(os.path.basename(path))[0]
    m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
    fmraw = m.group(1) if m else ""
    links = [
        l.split("|")[0].split("#")[0].strip()
        for l in re.findall(r"\[\[([^\]]+)\]\]", strip_code(txt))
    ]
    return {
        "name": name,
        "path": path,
        "has_fm": bool(m),
        "present": {k: bool(re.search(r"^%s:" % k, fmraw, re.M)) for k in FM_FIELDS},
        "aliases": parse_list_field(fmraw, "aliases"),
        "tags": parse_list_field(fmraw, "tags"),
        "type": scalar(fmraw, "type"),
        "status": scalar(fmraw, "status"),
        "links": links,
        "mermaid": txt.count("```mermaid"),
    }


def section(title):
    print("\n" + "=" * 62)
    print(title)
    print("=" * 62)


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "."
    if not os.path.isdir(base):
        sys.exit("Caminho inexistente: %s" % base)

    notes = {}
    alias_map = {}
    for p in find_notes(base):
        n = load(p)
        notes[n["name"]] = n
        for a in n["aliases"]:
            alias_map[a] = n["name"]

    inbound = collections.Counter()
    broken_by_source = collections.defaultdict(list)
    broken_targets = collections.Counter()

    for name, n in notes.items():
        for link in sorted(set(n["links"])):
            if link in notes:
                inbound[link] += 1
            elif link in alias_map:
                inbound[alias_map[link]] += 1
            else:
                broken_by_source[name].append(link)
                broken_targets[link] += 1

    total_links = sum(len(set(n["links"])) for n in notes.values())
    total_broken = sum(len(v) for v in broken_by_source.values())

    section("RESUMO")
    print("Notas do vault ............. %d" % len([n for n in notes if n not in ROOT_DOCS]))
    print("Docs de raiz ............... %d (README, CLAUDE, CHANGELOG)"
          % len([n for n in notes if n in ROOT_DOCS]))
    print("Wikilinks unicos ........... %d" % total_links)
    print("Links quebrados ............ %d (%d alvos distintos)"
          % (total_broken, len(broken_targets)))
    print("Notas orfas ................ %d"
          % sum(1 for n in notes if inbound[n] == 0 and n not in ROOT_DOCS))
    print("Notas sem links de saida ... %d"
          % sum(1 for n in notes.values() if not n["links"]))
    print("Diagramas Mermaid .......... %d"
          % sum(n["mermaid"] for n in notes.values()))

    section("LINKS QUEBRADOS POR ORIGEM")
    print("Concentracao alta numa nota = cluster em construcao (backlog).")
    print("Espalhamento por muitas notas = defeito real.\n")
    for name, links in sorted(broken_by_source.items(), key=lambda kv: -len(kv[1])):
        out = len(set(notes[name]["links"]))
        print("%4d/%-4d  %s" % (len(links), out, name))
        if len(links) <= 8:
            print("           -> %s" % ", ".join(sorted(links)))

    section("NOTAS ORFAS (sem links de entrada)")
    orphans = [n for n in sorted(notes) if inbound[n] == 0 and n not in ROOT_DOCS]
    if not orphans:
        print("nenhuma")
    for n in orphans:
        flag = "  <-- MOC ORFAO" if notes[n]["type"] == "moc" else ""
        print("  %-45s %s%s" % (n, notes[n]["path"], flag))

    section("NOTAS SEM LINKS DE SAIDA")
    dead = [n for n in sorted(notes) if not notes[n]["links"] and n not in ROOT_DOCS]
    print("  " + ("\n  ".join(dead) if dead else "nenhuma"))

    section("HUBS DO GRAFO (mais links de entrada)")
    for n, c in inbound.most_common(12):
        print("  %3d  %s" % (c, n))

    section("CONFORMIDADE DE FRONTMATTER")
    print("legenda: " + " ".join(f[:4] for f in FM_FIELDS) + "\n")
    missing = collections.Counter()
    for name in sorted(notes):
        if name in ROOT_DOCS:
            continue
        n = notes[name]
        row = "".join("Y" if n["present"][f] else "." for f in FM_FIELDS)
        for f in FM_FIELDS:
            if not n["present"][f]:
                missing[f] += 1
        if row != "Y" * len(FM_FIELDS):
            print("  %s  %s" % (row, name))
    print("\ncampos ausentes: %s" % (dict(missing.most_common()) or "nenhum"))

    section("VOCABULARIO CONTROLADO")
    bad_type = collections.defaultdict(list)
    bad_status = collections.defaultdict(list)
    for name, n in notes.items():
        if name in ROOT_DOCS:
            continue
        if n["type"] and n["type"] not in VALID_TYPE:
            bad_type[n["type"]].append(name)
        if n["status"] and n["status"] not in VALID_STATUS:
            bad_status[n["status"]].append(name)
    for label, bad, valid in (("type", bad_type, VALID_TYPE),
                              ("status", bad_status, VALID_STATUS)):
        print("\n%s valido: %s" % (label, ", ".join(sorted(valid))))
        if not bad:
            print("  tudo conforme")
        for value, names in sorted(bad.items(), key=lambda kv: -len(kv[1])):
            hint = LEGACY.get(value)
            arrow = "  -> migrar para '%s'" % hint if hint else ""
            print("  %-18s %d nota(s)%s" % (value, len(names), arrow))
            print("       %s" % ", ".join(sorted(names)[:6])
                  + (" ..." if len(names) > 6 else ""))

    section("TAXONOMIA DE TAGS")
    tags = collections.Counter()
    for n in notes.values():
        for t in n["tags"]:
            tags[t] += 1
    print("%d tags distintas para %d notas\n" % (len(tags), len(notes)))
    singles = [t for t, c in tags.items() if c == 1]
    for t, c in tags.most_common():
        if c > 1:
            print("  %3d  %s" % (c, t))
    print("\n  usadas uma unica vez (%d): %s" % (len(singles), ", ".join(sorted(singles))))

    norm = collections.defaultdict(set)
    for t in tags:
        key = re.sub(r"[^a-z]", "", t.lower()).replace("sser", "ser").replace("arqu", "arch")
        norm[key[:9]].add(t)
    dupes = {k: v for k, v in norm.items() if len(v) > 1}
    if dupes:
        print("\n  possiveis duplicatas semanticas:")
        for v in dupes.values():
            print("    %s" % " / ".join(sorted(v)))

    section("FIM")
    print("Regressao e o que importa: nenhuma alteracao deve criar orfas novas")
    print("nem links quebrados fora do cluster em construcao.")


if __name__ == "__main__":
    main()
