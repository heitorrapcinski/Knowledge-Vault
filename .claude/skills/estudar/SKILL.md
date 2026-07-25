---
name: estudar
description: Estuda uma fonte (livro, artigo, documento) e incorpora o conhecimento ao Knowledge Vault, produzindo notas de literatura, conceitos atômicos e conexões. Use quando o autor pedir para estudar, ler, processar ou extrair conhecimento de um material específico.
argument-hint: <caminho do arquivo, título da obra ou material já disponível no contexto>
---

# Estudar uma fonte

Incorpore o conhecimento da fonte ao Knowledge Vault seguindo o **Fluxo A** do `CLAUDE.md`.

**Fonte:** $ARGUMENTS

## Antes de escrever qualquer coisa

1. Leia `README.md` — é a fonte única das convenções (estrutura, tipos de nota, frontmatter, anatomia, nomenclatura, callouts).
2. Leia `CLAUDE.md` — o protocolo de trabalho.
3. Leia o MOC do domínio em `03 Maps of Content (MOCs)/`, se já existir.
4. Liste as notas existentes do cluster afetado e leia as mais relevantes.
5. Leia a fonte **por inteiro** antes de produzir a primeira nota.

## Execução

1. **Nota de literatura** em `01 Literature/Books/<Obra>/` — uma nota por capítulo ou parte, mais o índice da obra.
2. **Triagem de conceitos.** Para cada conceito apresentado, classifique explicitamente:
   - *já existe* → enriquecer a nota atual, preservando o que está lá
   - *novo e atômico* → criar nota em `Concepts/` ou `Practices/`
   - *sem valor fora da fonte* → fica apenas na nota de literatura

   Procure por nome de arquivo **e** por `aliases` antes de decidir que algo é novo.
3. **Notas permanentes.** Um conceito por nota, na anatomia correta do tipo.
4. **Registro no MOC** do domínio, no mesmo passo.
5. **Conexões.** Preencha `Veja também` / `Ref:` e procure ativamente pontes com os outros clusters do vault.
6. **`CHANGELOG.md`** — entrada datada em `[Não publicado]`, com as categorias corretas.
7. **`README.md`** — atualize a seção *Estado Atual* apenas se ela ficou desatualizada. Edição cirúrgica.
8. **Auditoria:** `python3 .claude/scripts/audit.py`. Corrija as regressões no cluster que você tocou.
9. **Commit semântico**, sem push.

## Regras

- Nunca duplique conceito existente.
- Nunca crie nota órfã — toda nota nasce com pelo menos um link de entrada.
- Nunca invente fato que não está na fonte. Lacuna vira `> [!question]` no MOC.
- Passou de ~10 notas novas: pare, apresente o faseamento e aguarde aprovação.
- Ao final, percorra a *Definition of Done* do `CLAUDE.md` item a item.

## Entrega

Relate: notas criadas, notas enriquecidas, conexões novas, lacunas registradas e o resultado da auditoria antes e depois.
