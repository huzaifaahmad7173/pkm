# Backend Agents Guide

Rules for working on the backend. Source of truth: the docs in this folder (`technologies.md`, `service-patterns.md`, `security.md`, `authentication.md`, `deployment.md`).

## Stack & Conventions

- **Python** is the primary language. Follow PEP 8, use the approved Python version, use virtual environments, keep code modular.
- **NumPy** for numerical work: prefer arrays and vectorized operations over loops.
- **OpenCV** for image/video processing; release camera resources; keep processing functions reusable.
- **MediaPipe** for real-time landmark/pose pipelines; reuse initialized models, process frames efficiently.
- **TensorFlow or PyTorch** (choose one) for deep learning; separate model definitions from training code; save checkpoints and document versions.
- **scikit-learn** for classic ML; split train/test properly, save trained models, use pipelines.
- **Pandas** for data analysis; keep cleaning reproducible; handle missing values explicitly.
- **Matplotlib** for charts; label clearly, use consistent styles, save figures in automated workflows.
- **Pillow** for image loading/resizing/conversion; close files, preserve quality.
- **python-dotenv** for `.env` loading; never commit `.env`, keep secrets out of source, maintain `.env.example`.

## Architecture (Service Patterns)

- Layer requests: **HTTP layer** (parse/validate/map errors — no business rules) → **Service layer** (business logic, transactions, framework-agnostic, unit-testable) → **Data access** (repositories/ORM, one query per concern) → database/external.
- Request flow: authenticate → authorize → validate input → run service logic → persist atomically in a transaction → return stable documented response.
- Define a single error model (code + message + details) and one error-to-HTTP mapping. Fail fast on validation; wrap unexpected exceptions (safe generic message to client, full details logged).
- Long-running jobs go on a queue/worker, not the request path. Use idempotency keys for retryable work; use the outbox pattern for reliable DB-write + emit-event.

## Security

- Validate everything server-side (client is untrusted); allowlists over blocklists; parameterized queries only; never trust upload paths.
- No secrets in code, committed config, or logs. Use env vars/secret manager; rotate on compromise; scan for leaked keys.
- Mitigate: SQL injection (parameterized/ORM), XSS (escape + CSP), CSRF (SameSite cookies/tokens), broken auth (enforce authz on every route), rate limiting, dependency vulns (pin + scan), PII/secret redaction in logs.
- Web backends: set `Content-Security-Policy`, `X-Content-Type-Options: nosniff`, `Strict-Transport-Security`, `X-Frame-Options: DENY`.

## Authentication

- Hash passwords with a slow salted algorithm (argon2id/bcrypt); never plaintext/MD5/SHA.
- Pick one mechanism (server sessions OR stateless tokens) and document it — don't mix.
- Tokens: short-lived access tokens (~15 min) + revocable refresh token; minimal non-sensitive claims; validate signature, expiry, issuer, audience on every request; never store in localStorage if XSS is a concern.
- HTTPS everywhere; cookies `HttpOnly`, `Secure`, `SameSite`; rate-limit login; account lockout/exponential backoff.
- Offer TOTP/passkeys when feasible; centralize identity through the IdP.

## Deployment

- Environments: `local`, `staging` (mirrors prod), `production`; config per environment via env vars, no hardcoded URLs.
- CI runs on every push (lint, typecheck, unit tests, build). CD deploys on merge to main (or manual for prod). Build artifacts once, promote them. Keep last N releases deployable for rollback.
- Release checklist: tests/linters green, migrations reviewed (see `../database/migrations.md`), feature flags for risky changes, secrets set, changelog updated.
- Observability: structured JSON logs with request IDs; metrics for request rate, latency percentiles, error rate, queue depth; `/health` endpoint; alert on error-rate/latency thresholds.
