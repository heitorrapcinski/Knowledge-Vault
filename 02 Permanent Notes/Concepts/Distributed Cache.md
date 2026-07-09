---
title: Distributed Cache
tags:
  - distributed-systems
  - performance
type: concept
status: evergreen
created: 2026-07-09
---
Distributed Cache é um cache compartilhado entre vários servidores.

Seu objetivo é reduzir a carga sobre bancos de dados e diminuir a latência.

```mermaid
graph TD

Client --> Cache

Cache --> Database
```

> [!tip]
> O cache deve armazenar apenas dados que possam ser reconstruídos.

## Benefícios

- Alta performance
- Escalabilidade
- Menor custo
- Menor latência

## Tecnologias

- Redis
- Memcached
- Hazelcast

## Veja também

- [[Caching]]
- [[Redis]]
- [[Performance]]