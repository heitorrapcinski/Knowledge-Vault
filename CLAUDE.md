# CLAUDE.md — Protocolo de Trabalho no Knowledge Vault

Este arquivo orienta agentes de IA que trabalham neste repositório. Ele define **o processo**: o que ler, em que ordem, como validar e quando parar.

> [!important] Regra Zero
> **As convenções do vault vivem no [README.md](README.md), não aqui.**
> Leia o README **antes de criar ou editar qualquer nota**. Ele é a fonte única de verdade sobre estrutura de pastas, tipos de nota, frontmatter, anatomia, nomenclatura e recursos permitidos.
> Se este arquivo e o README divergirem, **o README vence** — e a divergência deve ser reportada ao autor.

---

## 1. Sequência de leitura obrigatória

Nenhuma escrita acontece antes destes quatro passos. Não pule nenhum, mesmo em pedidos pequenos.

1. **`README.md`** — convenções, estrutura, tipos de nota, frontmatter, estado atual dos clusters.
2. **O MOC do domínio** em `03 Maps of Content (MOCs)/` — mostra o que já existe e onde a nova nota se encaixa.
3. **As notas existentes do cluster afetado** — para escrever no mesmo registro, reaproveitar vocabulário e evitar contradições.
4. **`CHANGELOG.md`** — mostra o que foi feito recentemente e o que ficou pendente.

> [!warning] Antiduplicação
> Antes de criar qualquer nota, **procure por ela**: pelo nome do arquivo, pelos `aliases` de todas as notas e por menções no corpo do vault.
> Conceito que já existe é **enriquecido**, nunca duplicado. Duas notas sobre o mesmo conceito são o pior defeito possível neste repositório.

---

## 2. Fluxos de trabalho

### Fluxo A — Estudar uma fonte (livro, artigo, documento, transcrição)

1. Ler a fonte por inteiro antes de escrever qualquer coisa.
2. Criar a nota de literatura em `01 Literature/Books/<Obra>/`, seguindo a anatomia do README. Uma nota por capítulo ou parte, mais um índice da obra.
3. Listar os conceitos apresentados. Para cada um, decidir: **já existe** (enriquecer), **é novo e atômico** (criar), ou **não tem valor fora da fonte** (fica só na nota de literatura).
4. Criar ou enriquecer as notas permanentes em `Concepts/` ou `Practices/`.
5. Registrar as notas novas no MOC do domínio. Se o domínio ainda não tem MOC e passou de 5 notas, propor a criação de um.
6. Conectar: preencher `Veja também` / `Ref:` e procurar ativamente pontes com clusters já existentes.
7. Atualizar `CHANGELOG.md` e, se a seção *Estado Atual* ficou desatualizada, o `README.md`.
8. Rodar a auditoria (seção 5) e corrigir o que ela apontar dentro do cluster tocado.

### Fluxo B — Pesquisar na internet

Vale tudo do Fluxo A, mais estas exigências:

- **Buscar antes de afirmar.** Nada de escrever de memória sobre estado atual de tecnologias, versões, specs ou produtos. Pesquise.
- **Múltiplas fontes.** Todo fato relevante precisa aparecer em pelo menos duas fontes independentes, ou ser marcado explicitamente como reivindicação de uma única fonte.
- **Priorizar fonte primária:** especificação oficial > documentação do fabricante > paper > post de engenharia > blog de terceiro.
- **Rastreabilidade obrigatória** no frontmatter:
  - `source:` nome da fonte e URL
  - `author:` autor real da fonte (não o assistente de IA)
  - `created:` data em que a nota foi escrita
- **Separar fato de interpretação.** Interpretação própria vai em callout `> [!success] Engineering View`, nunca misturada ao texto factual.
- Quando a pesquisa não conclui algo, registrar a lacuna em `> [!question]` no MOC do domínio, em vez de preencher com suposição.

### Fluxo C — Enriquecer uma nota existente

1. Ler a nota inteira e as notas que apontam para ela.
2. **Preservar o que já está lá.** Enriquecer é acrescentar e refinar, não reescrever do zero. Se algo precisa ser removido ou contradito, explicar o motivo ao autor.
3. Não alterar o nome do arquivo. Renomear quebra todos os `[[links]]` que apontam para a nota — se for realmente necessário, atualizar **todas** as referências na mesma alteração.
4. Não alterar `created`. Ele registra o nascimento da nota; a evolução é contada pelo CHANGELOG.
5. Promover o `status` quando a nota amadurecer (`seed` → `growing` → `evergreen`).

### Fluxo D — Manutenção do README

Atualize o `README.md` quando, e somente quando:

- a seção **Estado Atual** ficar desatualizada (contagem de notas, clusters, itens em construção);
- um **cluster novo** nascer ou um MOC novo for criado;
- uma **convenção mudar** — e nesse caso a mudança precisa de aprovação humana explícita.

Não reescreva o README inteiro para uma nota nova. Edição cirúrgica.

---

## 3. Regras invioláveis

1. **Nunca criar nota fora das quatro pastas numeradas.** Sem pastas novas na raiz sem aprovação.
2. **Nunca criar nota órfã.** Toda nota permanente nasce com pelo menos um link de entrada — normalmente do MOC do domínio.
3. **Nunca inventar fato.** Sem fonte, não entra. Na dúvida, registre como `> [!question]`.
4. **Nunca duplicar conceito.** Procure antes de criar.
5. **Nunca renomear ou mover nota** sem atualizar todos os links que apontam para ela.
6. **Nunca deixar links quebrados fora do cluster ativo.** Link para nota inexistente é sinalização de próxima leitura — só é legítimo dentro de um domínio em construção declarada.
7. **Nunca versionar `.obsidian/`.** É configuração local, não conhecimento.
8. **Nunca fazer `git push`** sem pedido explícito do autor.
9. **A curadoria final é humana.** O agente propõe; o autor decide o que fica no vault.

---

## 4. Definition of Done

Uma tarefa neste repositório só está concluída quando **todos** os itens abaixo forem verdadeiros:

- [ ] Frontmatter completo, com os 8 campos e vocabulário controlado do README (`type`, `status`)
- [ ] Nota atômica — um conceito por nota
- [ ] Anatomia correta para o tipo de nota
- [ ] Pelo menos um link de entrada e um de saída
- [ ] Registrada no MOC do domínio
- [ ] Pontes com outros clusters procuradas ativamente (e criadas, quando existirem)
- [ ] Fontes rastreáveis em `source` e `author`
- [ ] Auditoria executada, sem regressão em órfãs ou links quebrados
- [ ] `CHANGELOG.md` atualizado
- [ ] `README.md` atualizado, se a seção *Estado Atual* mudou
- [ ] Diagramas Mermaid com sintaxe válida
- [ ] Commit semântico feito (sem push)

---

## 5. Auditoria

Script de diagnóstico, sempre a partir da raiz do repositório:

```bash
python3 .claude/scripts/audit.py
```

Ele reporta: total de notas, links quebrados agrupados por origem, notas órfãs, notas sem links de saída, conformidade de frontmatter, valores de `type`/`status` fora do vocabulário e a taxonomia de tags com possíveis duplicatas semânticas.

**Como interpretar:** o objetivo não é zerar os números. Link quebrado dentro de um cluster em construção é intencional. Regressão é o que importa — nenhuma alteração deve criar órfãs novas nem links quebrados fora do cluster que está sendo trabalhado.

---

## 6. Estilo de escrita

- **Idioma:** português do Brasil. Termos técnicos consagrados permanecem em inglês (*Circuit Breaker*, *Data Lake*, *Bounded Context*).
- **Registro:** direto e denso. O vault é para consulta, não para leitura linear — sem introduções longas, sem repetir o óbvio, sem encher linguiça.
- **Prosa curta + estrutura.** Explique em prosa, organize em listas e tabelas. Nunca só bullets soltos.
- **Sempre que um conceito for confundível com outro, escreva a tabela comparativa.** É o recurso mais valioso do vault.
- **Diagrama só quando esclarece.** Mermaid decorativo é ruído.
- **Callouts com a semântica definida no README** — não decorativos.

---

## 7. Commits

Convenção semântica escopada no vault (detalhes no README):

| Prefixo | Uso |
|---|---|
| `feat(vault):` | Notas novas ou cluster novo |
| `docs(vault):` | Enriquecimento de notas existentes |
| `refactor(vault):` | Renomear, mover ou reorganizar |
| `fix(vault):` | Links quebrados, frontmatter, tipografia |
| `chore(vault):` | Configuração, whitespace, manutenção |

Um commit por unidade de conhecimento. Cluster novo é um commit; normalização de whitespace é outro. **Nunca misturados.**

### Quem pode executar git

O comportamento depende de **onde o agente está rodando** — verifique antes de executar qualquer comando git.

| Agente rodando | Git |
|---|---|
| **No computador do autor** (Cowork local, Claude Code, terminal) | Pode executar normalmente, seguindo as convenções acima. `push` continua exigindo pedido explícito |
| **Na nuvem, através da ponte remota** | **Não execute nenhum comando git neste repositório** |

> [!warning] Por que o agente remoto não pode usar git aqui
> A ponte remota permite criar, ler e mover arquivos, mas **bloqueia deletar** — é uma proteção do mecanismo, não uma configuração. O git depende de apagar seus próprios arquivos `.lock` ao final de cada operação de escrita. Esse passo falha silenciosamente e o lock fica preso, travando o Git do editor do autor com *"Another git process seems to be running"*.
>
> **O que o agente remoto faz no lugar:** escreve os arquivos, atualiza o `CHANGELOG.md` e entrega a mensagem de commit pronta para o autor executar.

> [!tip] Recuperação de lock preso
> Apagar `.git/*.lock` e `.git/objects/*.lock` com o repositório fechado no editor. Nenhum trabalho é perdido — os locks são arquivos vazios de controle.

---

## 8. Quando parar e perguntar

Interrompa e consulte o autor quando:

- a tarefa exigir **mudar uma convenção** do README;
- houver **contradição entre fontes** sobre um fato relevante;
- for necessário **renomear ou remover** uma nota existente;
- a fonte for **ambígua ou insuficiente** para uma nota atômica honesta;
- o trabalho passar de **~10 notas novas** — proponha um faseamento antes de executar;
- o pedido implicar **push, criação de branch ou alteração de histórico**.

---

## 9. Skills disponíveis

| Skill | O que faz |
|---|---|
| `/estudar <fonte>` | Fluxo A — lê uma fonte e produz literatura + conceitos + conexões |
| `/pesquisar <tema>` | Fluxo B — pesquisa na web e produz notas rastreáveis |
| `/auditar` | Diagnóstico de saúde do vault e plano de correção priorizado |
| `/conectar [cluster]` | Procura e cria pontes entre clusters isolados |

Definições em `.claude/skills/<nome>/SKILL.md`.

> [!important] Skills, não commands
> Este é o formato reconhecido tanto pelo **Cowork** quanto pelo **Claude Code**. O caminho legado `.claude/commands/*.md` funciona apenas no Claude Code — o Cowork o ignora. Ao criar um fluxo novo, use sempre `.claude/skills/`.
