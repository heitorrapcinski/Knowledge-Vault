---
title: Observability
aliases:
  - Observabilidade
tags:
  - itil
  - operations
  - engineering
type: concept
status: growing
source: ITIL Foundation (Version 5), PeopleCert, 2026
author: PeopleCert
created: 2026-07-25
---
> [!abstract]
> Observability é a propriedade de um sistema que permite entender seu estado interno a partir de seus sinais externos — incluindo estados que ninguém previu.

## Conceito

A diferença para monitoramento é a natureza da pergunta. Monitoramento responde perguntas **conhecidas** ("a CPU passou de 80%?"); observabilidade permite formular perguntas **novas** durante a investigação ("por que só usuários deste plano, nesta região, depois da última entrega?").

Sistemas distribuídos falham de formas que ninguém antecipou, o que torna dashboards pré-definidos insuficientes por construção.

## Pilares

| Pilar | O que revela |
|---|---|
| **Logs** | O que aconteceu, em detalhe |
| **Métricas** | Tendência agregada ao longo do tempo |
| **Traces** | Caminho da requisição entre serviços |

## Características

- Precisa ser embutida em [[Build (Lifecycle)]], não adicionada depois
- Base para reduzir [[Mean Time to Restore (MTTR)]]
- Insumo de [[Service Level Indicator (SLI)]] e de [[AIOps]]

## Veja também

- [[Monitoring and Event Management]]
- [[Site Reliability Engineering (SRE)]]
- [[Service Level Indicator (SLI)]]
- [[AIOps]]
- [[Digital Experience]]
