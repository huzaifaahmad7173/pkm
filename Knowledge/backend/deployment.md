# Deployment

How the backend gets built, released, and monitored.

## Environments

- Standard set: `local`, `staging` (mirrors prod), `production`.
- Staging is a smoke-test copy of prod; features land there before prod.
- Config per environment via env vars; no hardcoded URLs.

## CI/CD

- CI runs on every push: lint, typecheck, unit tests, build.
- CD deploys on merge to the main branch (or manual trigger for prod).
- Artifacts are built once and promoted, not rebuilt per environment.
- Rollbacks: keep the last N releases deployable; prefer forward fixes for data changes.

## Release Checklist

- [ ] Tests and linters green
- [ ] Migrations reviewed and ordered safely (see `database/migrations.md`)
- [ ] Feature flags if the change is risky
- [ ] Secrets for the target environment set
- [ ] Changelog/release notes updated

## Observability

- Structured logs (JSON) with request IDs.
- Metrics: request rate, latency percentiles, error rate, queue depth.
- Health endpoint `/health` for load balancers and orchestrators.
- Alerts on error-rate and latency thresholds, not just on outages.

## Fill In Per Project

- [ ] Hosting (VPS, container platform, serverless, ...)
- [ ] Orchestration (Docker Compose, Kubernetes, ...)
- [ ] Log/metrics stack (Grafana, Datadog, CloudWatch, ...)
- [ ] Deploy command(s) and who can trigger prod deploys
