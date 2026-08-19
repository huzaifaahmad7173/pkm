---
name: api
description: Use when working on or writing about the backend API — FastAPI endpoints, REST URL/method conventions, request/response envelopes, versioning, endpoint catalog, or API performance.
---

# API Knowledge

Pointer to the vault's API knowledge. Read the source docs before applying API rules; do not rely on memory.

## When to use

- Designing, building, or reviewing API endpoints (FastAPI).
- Questions on REST conventions, request/response format, error envelopes, versioning, or the endpoint catalog.
- API security, performance, and documentation practices.

## Where the knowledge lives

- Source of truth: `Knowledge/api/AGENTS.md`.
- Docs:
  - `Knowledge/api/api-overview.md`
  - `Knowledge/api/design-standards.md`
  - `Knowledge/api/endpoint-catalog.md`
  - `Knowledge/api/request-response.md`
  - `Knowledge/api/versioning.md`
  - `Knowledge/api/performance.md`
  - `Knowledge/api/technologies.md`

## Scope boundary

This skill covers the API contract and framework layer (FastAPI, REST conventions, request/response, versioning, catalog). For backend architecture and operations (service patterns, security, authentication, deployment), use the `backend` skill.

## How to use

1. Read `Knowledge/api/AGENTS.md` for the stack and key rules.
2. Read the specific doc relevant to the task (endpoints → `endpoint-catalog.md`, format → `request-response.md`, etc.).
3. Apply the rules as written in those files; treat them as authoritative.