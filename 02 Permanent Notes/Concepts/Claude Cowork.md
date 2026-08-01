---
title: Claude Cowork
aliases:
  - Cowork
tags:
  - ai
  - claude
  - agent
  - workflow
type: concept
status: seed
source: Claude 101 — Anthropic Academy
author: Anthropic
created: 2026-07-31
---
> [!abstract]
> **Claude Cowork** é a superfície do Claude dedicada ao trabalho delegado: você descreve um resultado multi-etapa e o Claude planeja, executa e devolve o entregável — com acesso a pastas locais, ferramentas conectadas e execução agendada.

## Conceito

Cowork é a materialização de [[Agentic Workflow]] no app desktop do Claude. A diferença concreta em relação ao Chat está no **destino do arquivo**: o Chat lê o que você envia e devolve download; o Cowork aponta para uma pasta sua, lê o que está lá e **salva o trabalho de volta no mesmo lugar**.

## Capacidades

| Capacidade | O que faz |
|---|---|
| **Acesso a pasta local** | Lê e escreve na pasta que você seleciona |
| **[[Scheduled Task\|Tarefas agendadas]]** | Executa em cadência definida; se o app estava fechado, recupera depois |
| **Subagentes** | Divide um trabalho grande entre workers paralelos com contexto próprio — ver [[Agentes Paralelos]] |
| **Projetos** | Agrupa tarefas relacionadas num workspace com arquivos, instruções e memória — ver [[Project Workspace]] |
| **Uso de navegador** | Navega sites e traz o achado para dentro da tarefa |
| **[[Computer Use]]** | Opera o computador quando não existe conector (research preview) |
| **[[Plugin (AI Agent)\|Plugins]]** | Pacotes de skills, conectores e agentes por tipo de trabalho |

## Características

- **Orientado a entregável** — a saída é um arquivo no seu disco, não texto no chat
- **Observável** — plano visível, fontes consultadas, progresso acompanhável, interrompível
- **Com pontos de parada** — pede aprovação nas ações irreversíveis
- **Programável no tempo** — a tarefa recorrente é cidadã de primeira classe

> [!question] Lacuna aberta
> O curso Claude 101 apresenta o Cowork em visão geral. A profundidade — governança de permissões, limites de subagente, padrões de composição com [[Agent Skill|Skills]] e [[Plugin (AI Agent)|plugins]] — está no curso *Introduction to Claude Cowork*, ainda não incorporado a este vault.

## Veja também

- [[Agentic Workflow]]
- [[Claude Code]]
- [[Escolha da Forma de Trabalho com IA]]
- [[Agent Skill]]
- [[Connector]]
