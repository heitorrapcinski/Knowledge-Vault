# Changelog

Registro das mudanças no Engineering Knowledge Vault.

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/), adaptado a uma base de conhecimento: em vez de versões de software, as entradas são **datadas pelo dia do estudo**.

**Categorias**

| Categoria | Uso |
|---|---|
| `Adicionado` | Notas novas |
| `Enriquecido` | Notas existentes ampliadas ou refinadas |
| `Conectado` | Links, pontes entre clusters, MOCs atualizados |
| `Estrutura` | Pastas, convenções, README, tooling |
| `Corrigido` | Links quebrados, frontmatter, tipografia |
| `Removido` | Notas removidas ou fundidas |

`[Não publicado]` reúne o que já está no disco mas ainda não foi enviado ao repositório remoto.

---

## [Não publicado]

### Estrutura

- `CLAUDE.md` criado — protocolo de trabalho para agentes de IA, com sequência de leitura obrigatória, quatro fluxos (estudar fonte, pesquisar na web, enriquecer nota, manter README), regras invioláveis e *definition of done*. O README permanece como fonte única das convenções.
- `CHANGELOG.md` criado — este arquivo, com o histórico reconstruído a partir do Git e das datas de criação das notas.
- Comandos de agente adicionados em `.claude/commands/`: `/estudar`, `/pesquisar`, `/auditar` e `/conectar`.
- Script de auditoria adicionado em `.claude/scripts/audit.py` — reporta links quebrados por origem, notas órfãs, conformidade de frontmatter e taxonomia de tags.
- `README.md` reescrito para refletir a estrutura real do vault. Passou a documentar a anatomia de cada tipo de nota, as regras de nomenclatura, os três mecanismos de conexão, a semântica dos callouts, os tipos de diagrama Mermaid em uso e o inventário dos quatro clusters. Vocabulário controlado definido para `type` (`literature`, `concept`, `practice`, `moc`, `project`) e `status` (`seed`, `growing`, `evergreen`).

### Pendente

- Migrar o vocabulário herdado: `permanent-note` → `concept`, `project-case` → `project`, `status: permanent` e `status: moc` → `evergreen`.
- Completar o frontmatter das 24 notas anteriores a 09/07, que ainda não seguem o padrão de 8 campos.
- Refatorar o MOC `ITIL 5`: dos seus 150 links, 142 apontam para notas inexistentes. Separar o escopo ativo do backlog de estudo.
- Escrever as 5 notas da camada multiagente para fechar o cluster de IA.
- Criar um ponto de entrada na raiz que ligue os três MOCs — hoje todos estão órfãos no grafo.

---

## 2026-07-25

### Estrutura

- Dois commits registraram no Git todo o trabalho de julho, que estava apenas no disco: as 15 notas dos clusters de IA e ITIL, e a normalização de fim de linha de 20 arquivos do cluster de Lean Inception.

### Diagnóstico

Primeira auditoria completa do vault — 64 arquivos, 366 wikilinks únicos:

- 200 links quebrados, dos quais 142 concentrados apenas no MOC `ITIL 5`
- 11 notas órfãs, incluindo os três MOCs
- 4 clusters temáticos sem nenhuma ponte entre si
- 90 tags para 63 notas, com duplicatas semânticas (`architecture`/`arquitetura`, `microservices`/`microsserviços`)
- `source` ausente em 55 notas e `author` em 54

---

## 2026-07-24

### Adicionado

- Cluster **ITIL e Service Management** iniciado, com 5 notas de conceito: `ITIL`, `IT Service Management (ITSM)`, `Service Management`, `Digital Organization` e `Digital Ecosystem`.

### Conectado

- MOC `ITIL 5` criado, organizando o domínio em Foundations, Service Value System, Service Value Chain, Guiding Principles, Governance, Products, Services, Experience, Practices, Engineering, Architecture, Data & AI e Métricas.

---

## 2026-07-17

### Adicionado

- Cluster **IA Generativa e Agentes** criado, com 8 notas de conceito: `Large Language Model (LLM)`, `Retrieval-Augmented Generation (RAG)`, `Knowledge Graph`, `Context Graph`, `Model Context Protocol (MCP)`, `Harness`, `Agent Runtime` e `Agent Supervisor`.
- Tabelas comparativas estabelecidas como recurso central do vault: *Knowledge Graph × Context Graph* e *Harness × Agent Runtime*.

### Conectado

- MOC `AI Generative Architecture` criado, organizando o domínio em cinco camadas: raciocínio, conhecimento, contexto, execução e colaboração.

---

## 2026-07-09

### Adicionado

- Cluster **Cloud, Dados e Resiliência** expandido para 24 notas de conceito:
  - **Armazenamento:** `Storage`, `Block Storage`, `File Storage`, `Object Storage`
  - **Resiliência:** `Disaster Recovery`, `Business Continuity`, `High Availability`, `Backup`, `RPO`, `RTO`, `Risk Management`
  - **Dados:** `Data Lake`, `Data Warehouse`, `ETL`, `ELT`, `Business Intelligence`
  - **Sistemas distribuídos:** `CAP Theorem`, `Circuit Breaker`, `Event Sourcing`, `Distributed Cache`, `Service Mesh`
  - **Infraestrutura e segurança:** `CIDR`, `Identity Federation`
  - **Organização:** `Lei de Conway`

### Estrutura

- Frontmatter de 8 campos adotado como padrão a partir deste ponto.

---

## 2026-07-07

### Adicionado

- Vault criado com a estrutura PARA de quatro pastas numeradas.
- Cluster **Lean Inception** completo, a partir do livro de Paulo Caroli:
  - 4 notas de literatura (índice da obra e três partes)
  - 13 práticas de workshop, de `Visão do Produto` a `Canvas MVP`
  - 5 conceitos: `MVP`, `Personas`, `Jornadas do Usuário`, `Funil de Vendas - AARRR`, `Ciclo Construir-Medir-Aprender`
  - MOC `Lean Inception MOC`
  - Estudo de caso `Estudo de Caso - Easy-bola`
- README inicial com os princípios do vault: Atomic Notes, Evergreen Notes, Zettelkasten, PARA, Second Brain e curadoria assistida por IA.
