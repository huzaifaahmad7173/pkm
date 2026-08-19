# Service Patterns

Generic backend architecture: how requests flow and where logic lives.

## Layering

```
HTTP layer (routes/controllers)
        |
        v
Service layer (business logic, transactions)
        |
        v
Data access layer (repositories, ORM, queries)
        |
        v
Database / external systems
```

- **HTTP layer**: parse input, validate shape, map errors to HTTP codes. No business rules.
- **Service layer**: business rules, orchestration, invariants. Framework-agnostic and unit-testable.
- **Data access**: one query per concern, no raw SQL scattered through services.

## Request Flow Checklist

1. Authenticate (who is calling?)
2. Authorize (are they allowed to do this?)
3. Validate input (shape, types, ranges)
4. Run business logic in a service
5. Persist changes atomically (transaction)
6. Return a stable, documented response shape

## Errors

- Define an error model (code + message + optional details) and a single error-to-HTTP mapping.
- Fail fast: return early on validation errors, never continue with bad data.
- Wrap unexpected exceptions; surface a safe generic message to clients, log the details.

## Async Work

- Long-running jobs go on a queue/worker, not in the request path.
- Idempotency keys for anything retryable (payments, webhooks, imports).
- Outbox pattern if you need "DB write + emit event" to be reliable.

## Fill In Per Project

- [ ] Folder/module layout (e.g., `routes/ services/ repositories/ models/`)
- [ ] Dependency injection or module pattern in use
- [ ] Queue/worker tooling (BullMQ, Celery, SQS, ...)
