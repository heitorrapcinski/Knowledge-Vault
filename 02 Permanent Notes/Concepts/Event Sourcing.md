---
title: Event Sourcing
tags:
  - architecture
  - distributed-systems
type: concept
status: evergreen
created: 2026-07-09
---
Event Sourcing é um padrão onde o estado da aplicação é reconstruído a partir da sequência de eventos ocorridos.

Em vez de armazenar apenas o estado atual, armazenam-se todos os eventos.

```mermaid
graph LR

Command --> EventStore

EventStore --> Projection

Projection --> ReadModel
```

> [!info]
> O histórico completo da aplicação fica preservado.

## Benefícios

- Auditoria
- Replay
- Rastreabilidade
- Integração por eventos

## Desafios

- Complexidade
- Evolução de eventos
- Projeções

## Veja também

- [[CQRS]]
- [[Event Driven Architecture]]
- [[Domain Events]]