# Database Agents Guide

Rules for working with the database. Source of truth: the docs in this folder (`technology.md`, `schema-conventions.md`, `query-patterns.md`, `migrations.md`, `backup-restore.md`).

## Technology

- **SQLite3** (built into Python) is the database: serverless, single-file, zero-config, ACID-compliant.
- Use it for small/medium apps, prototypes, local dev, low write concurrency. Move to PostgreSQL/MySQL when you need high write concurrency, scale, HA/replication, or advanced admin features.
- Enable foreign key support. Keep one connection per application context; close connections after use; handle database exceptions and roll back failed transactions.

## Schema Conventions

- **Tables**: plural, `snake_case` (`users`, `order_items`). **Columns**: `snake_case` (`created_at`, `first_name` — never `createdAt`).
- Every table has an `id` primary key — pick UUID or auto-increment and stay consistent.
- Foreign keys named `<singular>_id` (`user_id`, `order_id`, `product_id`).
- Timestamps: `created_at`, `updated_at`, optional `deleted_at`.
- Money → `DECIMAL`, never `FLOAT`. Use timezone-aware timestamps. Booleans prefixed `is_` / `has_` / `can_`.
- Enforce constraints at the DB level (PRIMARY/FOREIGN/UNIQUE/CHECK/NOT NULL); don't rely on app validation.
- If using soft deletes, every query must ignore deleted rows unless explicitly requested.
- Document ER diagrams, relationships, constraints, status/enum values.

## Query Patterns

- Select only required columns; no `SELECT *`; filter early; use indexes; parameterize queries; avoid duplicate queries.
- Pagination: offset for small datasets (`LIMIT 20 OFFSET 40`); cursor for large/infinite scroll.
- Prefer joins over multiple queries; avoid N+1.
- Use transactions for multi-row writes, money transfers, inventory updates.
- Cache settings, categories, permissions, frequently read data. Avoid caching fast-changing data without a clear invalidation strategy.
- Monitor slow queries, durations, missing indexes, execution plans.

## Migrations

- Every schema change is version controlled; never edit applied migrations; keep migrations small and repeatable; review in code review.
- Name sequentially: `0001_create_users.sql`, `0002_add_orders_table.sql`.
- One change per migration. Every migration should support rollback. Separate schema changes from data-migration scripts.
- Deployment order: merge code → deploy → run migrations → verify → start application.
- Avoid: large table locks, NOT NULL without defaults, missing indexes, long-running migrations.

## Backup & Restore

- Back up by copying the database file, but stop writes first (stop app or ensure no writes in progress), then verify the copy.
- Restore: stop app → keep a copy of the current DB → replace the file with the backup → restart → verify data intact.
- Store backups securely (local/external/cloud); keep multiple copies; test restores periodically; never overwrite the only backup.
