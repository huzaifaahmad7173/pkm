# Database Migrations

Migrations keep database schema synchronized with application code.

---

# Principles

- Every schema change is version controlled.
- Never edit applied migrations.
- Every migration should be repeatable.
- Keep migrations small.
- Review migrations during code review.

---

# Naming

Examples

0001_create_users.sql

0002_add_orders_table.sql

0003_add_user_indexes.sql

---

# Best Practices

## One Change Per Migration

Good

- Create table

Bad

- Create table
- Rename columns
- Insert data
- Add indexes

---

## Rollbacks

Every migration should support rollback when possible.

---

## Data Migrations

Separate schema changes from data migration scripts.

---

## Deployment Workflow

1. Merge code
2. Deploy
3. Run migrations
4. Verify
5. Start application

---

# Common Mistakes

- Large table locks
- NOT NULL without defaults
- Missing indexes
- Long-running migrations

---

# Checklist

- Migration reviewed
- Rollback available
- Tested locally
- Tested in staging
- Documentation updated