---
name: auditar
description: Diagnostica a saúde do Knowledge Vault — notas órfãs, links quebrados, conformidade de frontmatter, vocabulário e tags — e propõe um plano de correção priorizado. Use quando o autor pedir auditoria, diagnóstico, verificação de consistência ou estado de saúde do vault.
argument-hint: "[cluster ou pasta a auditar — opcional, padrão: vault inteiro]"
---

# Auditar o vault

Diagnostique a saúde do Knowledge Vault e proponha um plano de correção.

**Escopo:** $ARGUMENTS (vazio = vault inteiro)

## Execução

1. Leia `README.md` para saber quais são as convenções vigentes — a auditoria mede aderência a elas, não a um padrão genérico.
2. Rode o diagnóstico:

   ```bash
   python3 .claude/scripts/audit.py
   ```

3. Verifique o que o script não cobre:
   - **Atomicidade** — notas cobrindo mais de um conceito
   - **Duplicação semântica** — conceitos iguais com nomes diferentes
   - **Sintaxe Mermaid** inválida
   - **Aderência de anatomia** ao tipo declarado em `type`
   - **Isolamento de clusters** — domínios sem nenhuma ponte entre si
4. Cheque o estado do Git: alterações não commitadas e commits não enviados.

## Como interpretar

**O objetivo não é zerar os números.** Link quebrado dentro de um cluster em construção declarada é intencional — sinaliza a próxima nota a escrever. O que importa é distinguir:

- **Defeito** — órfã, duplicata, frontmatter inválido, link quebrado espalhado fora de um cluster ativo, MOC órfão
- **Backlog saudável** — link quebrado concentrado num domínio em construção
- **Regressão** — qualquer coisa que piorou em relação à última auditoria registrada no `CHANGELOG.md`

## Entrega

Um relatório com:

1. **Números-chave** e a variação desde a última auditoria registrada no CHANGELOG
2. **Defeitos**, ordenados por impacto na navegabilidade do vault
3. **Backlog saudável**, separado dos defeitos e nomeando o cluster de cada item
4. **Plano priorizado** — o que corrigir primeiro e o esforço estimado de cada item

**Não execute correções sem aprovação.** Apresente o plano e aguarde. A única exceção é a atualização do `CHANGELOG.md` com o resultado do diagnóstico, que pode ser feita direto.
