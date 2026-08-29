---
title: Query Patterns
description: Writing efficient queries improves performance and scalability.
tags:
  - database
  - query-patterns
status: Draft
---

# Query Patterns

Writing efficient queries improves performance and scalability.

---

# General Rules

- Select only required columns.
- Filter early.
- Use indexes.
- Avoid SELECT *.
- Parameterize queries.
- Avoid duplicate queries.

---

# Pagination

## Offset Pagination

Suitable for:

- Small datasets

Example

LIMIT 20 OFFSET 40

---

## Cursor Pagination

Suitable for:

- Large datasets
- Infinite scrolling

---

# Joins

Prefer joins over multiple queries.

Avoid N+1 queries.

---

# Transactions

Use transactions when:

- Multiple inserts
- Multiple updates
- Money transfers
- Inventory updates

---

# Caching

Cache:

- Settings
- Categories
- Permissions
- Frequently read data

Avoid caching frequently changing data unless invalidation is well understood.

---

# Monitoring

Track:

- Slow queries
- Query duration
- Missing indexes
- Execution plans

---

# Checklist

- Indexed columns
- Parameterized
- Pagination
- No N+1
- Query plan reviewed