---
name: pesquisar
description: Pesquisa um tema na internet com fontes primárias e verificação cruzada, e produz notas rastreáveis no Knowledge Vault. Use quando o autor pedir para pesquisar, investigar ou buscar informação atual sobre um tema para incorporar ao vault.
argument-hint: <tema a pesquisar>
---

# Pesquisar um tema

Pesquise na internet e incorpore o resultado ao Knowledge Vault seguindo o **Fluxo B** do `CLAUDE.md`.

**Tema:** $ARGUMENTS

## Antes de escrever qualquer coisa

1. Leia `README.md` — fonte única das convenções.
2. Leia `CLAUDE.md` — o protocolo de trabalho.
3. Leia o MOC do domínio e as notas existentes do cluster afetado. **O vault pode já cobrir parte do tema** — nesse caso o trabalho é enriquecer, não criar.

## Pesquisa

- **Pesquise antes de afirmar.** Não escreva de memória sobre versões, specs, produtos ou estado atual de tecnologias.
- **Hierarquia de fontes:** especificação oficial > documentação do fabricante > paper revisado > post de engenharia da empresa responsável > blog de terceiro.
- **Verificação cruzada:** todo fato relevante precisa de duas fontes independentes. O que só tiver uma fonte deve ser marcado como tal no texto.
- **Datas importam.** Este é um domínio que muda rápido — verifique quando a fonte foi publicada ou atualizada pela última vez.
- **Contradição entre fontes:** não escolha um lado sozinho. Registre as duas posições e pergunte ao autor.

## Escrita

1. Notas atômicas em `Concepts/` ou `Practices/`, na anatomia do README.
2. **Rastreabilidade obrigatória no frontmatter:**
   - `source:` nome da fonte + URL
   - `author:` autor real da fonte — nunca o assistente de IA
   - `created:` data em que a nota foi escrita
3. **Separe fato de interpretação.** Análise própria vai em `> [!success] Engineering View`, jamais misturada ao texto factual.
4. Se um conceito é confundível com outro, escreva a tabela comparativa.
5. Registre as notas no MOC do domínio e conecte com `Veja também` / `Ref:`.
6. O que a pesquisa não conseguiu concluir vira `> [!question]` no MOC — não preencha com suposição.
7. Atualize `CHANGELOG.md` e, se necessário, a seção *Estado Atual* do `README.md`.
8. Rode `python3 .claude/scripts/audit.py` e corrija as regressões.
9. Commit semântico, sem push.

## Entrega

Relate: notas criadas ou enriquecidas, **as fontes usadas com URL**, os pontos que ficaram com fonte única, as contradições encontradas e as lacunas registradas.
