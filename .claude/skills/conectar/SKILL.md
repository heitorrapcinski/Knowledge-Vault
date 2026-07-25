---
name: conectar
description: Procura e cria pontes entre clusters isolados do Knowledge Vault, resolvendo notas órfãs e transformando ilhas temáticas em rede. Use quando o autor pedir para conectar notas, resolver órfãs, criar links entre domínios ou melhorar o grafo do vault.
argument-hint: "[cluster de origem — opcional, padrão: todos]"
---

# Conectar clusters

Procure conexões que deveriam existir no Knowledge Vault e ainda não existem.

**Escopo:** $ARGUMENTS (vazio = todos os clusters)

## Por que esta skill existe

O valor de um Zettelkasten está nas conexões, não nas notas. Um vault cujos domínios não se tocam é um conjunto de resumos organizados — não uma rede de conhecimento. Esta skill ataca especificamente o isolamento entre clusters.

## Execução

1. Leia `README.md` (convenções e inventário dos clusters) e `CLAUDE.md` (protocolo).
2. Mapeie os clusters existentes e as conexões atuais entre eles:

   ```bash
   python3 .claude/scripts/audit.py
   ```

3. Para cada par de clusters, procure ativamente por:
   - **Mesmo conceito, vocabulários diferentes** — o mesmo fenômeno com nome distinto em cada domínio
   - **Relação de causa** — um conceito de um domínio explica outro
   - **Tensão produtiva** — dois domínios prescrevendo coisas opostas, o que rende uma nota comparativa própria
   - **Ancestralidade** — um conceito é a origem histórica ou a generalização do outro
4. Verifique também as **notas órfãs** e as **notas sem links de saída**: cada uma é uma conexão que faltou.

## Tipos de ponte aceitáveis

| Ponte | Quando usar |
|---|---|
| Link em `Veja também` | Conceitos vizinhos, relação direta e óbvia |
| Link inline no corpo | O outro conceito é *usado* na explicação |
| Tabela comparativa | Os conceitos são confundíveis entre si |
| Nota nova de ligação | A relação é rica o bastante para ser um conceito próprio |
| Entrada em MOC | O conceito pertence de fato a mais de um domínio |

## Regras

- **Ponte precisa ser real.** Link só existe se a relação for defensável em uma frase. Conectar por conectar polui o grafo e é pior do que não conectar.
- Ao criar nota nova de ligação, ela segue todas as convenções do README como qualquer outra.
- Não altere o significado de notas existentes para forçar uma conexão.

## Entrega

1. **Mapa das conexões propostas**, cada uma com a justificativa em uma frase
2. **Pontes criadas**, separadas das apenas sugeridas
3. **Órfãs resolvidas** e as que permaneceram, com o motivo
4. `CHANGELOG.md` atualizado na categoria `Conectado`
5. Commit semântico `docs(vault):`, sem push
