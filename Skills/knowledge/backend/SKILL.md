---
name: backend
description: Use when working on or writing about the backend — Python stack, service patterns/architecture, security, authentication, or deployment.
---

# Backend Knowledge

Pointer to the vault's backend knowledge. Read the source docs before applying backend rules; do not rely on memory.

## When to use

- Building or reviewing Python backend code and services.
- Questions on service/request layering, security, authentication, or deployment.
- Backend environment and release/observability setup.

## Where the knowledge lives

- Source of truth: `Knowledge/backend/AGENTS.md`.
- Docs:
  - `Knowledge/backend/technologies.md`
  - `Knowledge/backend/service-patterns.md`
  - `Knowledge/backend/security.md`
  - `Knowledge/backend/authentication.md`
  - `Knowledge/backend/deployment.md`

## Scope boundary

This skill covers Python architecture and operations (stack, service patterns, security, auth, deployment). For the API contract and framework layer (FastAPI, REST endpoints, request/response, versioning), use the `api` skill.

## How to use

1. Read `Knowledge/backend/AGENTS.md` for the stack and key rules.
2. Read the specific doc relevant to the task (patterns → `service-patterns.md`, auth → `authentication.md`, etc.).
3. Apply the rules as written in those files; treat them as authoritative.
4. Migrations/deployment tie into `Knowledge/database/migrations.md` — see the `database` skill.