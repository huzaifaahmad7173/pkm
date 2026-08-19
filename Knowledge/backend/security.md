# Security

Baseline security practices for any backend.

## Input Validation

- Validate on the server, always — the client is untrusted.
- Allowlists over blocklists for fields, file types, and formats.
- Parameterized queries only; no string-built SQL.
- Never trust file names or upload paths; serve uploads from a dedicated bucket/path.

## Secrets

- No secrets in code, config files committed to git, or logs.
- Environment variables or a secret manager; rotate on compromise.
- `.env` files are never committed; keep a `.env.example` instead.
- Scan repos for accidentally committed keys.

## Common Mitigations

| Threat                | Mitigation                                        |
| --------------------- | ------------------------------------------------- |
| SQL injection         | Parameterized queries / ORM                       |
| XSS (API-driven UI)   | Escape output, CSP headers                        |
| CSRF                  | SameSite cookies, CSRF tokens                     |
| Broken auth           | Enforce auth + authorization checks on every route|
| Rate limiting         | Per-user and per-IP limits on sensitive endpoints |
| Dependency vulns      | Pin versions, automated dependency scanning       |
| Logging PII/secret    | Redact emails, tokens, passwords in logs          |

## Headers (Web Backends)

- `Content-Security-Policy`
- `X-Content-Type-Options: nosniff`
- `Strict-Transport-Security`
- `X-Frame-Options: DENY`

## Fill In Per Project

- [ ] Secret storage solution and rotation process
- [ ] Rate limiter in use and default limits
- [ ] Vulnerability scanning setup (dependabot, snyk, etc.)
- [ ] Incident/security contact process
