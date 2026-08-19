# Schema Conventions

Database schema should be predictable and consistent.

---

# Naming

## Tables

- plural
- snake_case

Examples

users

order_items

invoice_payments

---

## Columns

Use snake_case.

Good

created_at

updated_at

first_name

Bad

createdAt

FirstName

---

# Primary Keys

Every table should have

id

Choose one:

- UUID
- Auto Increment

Be consistent.

---

# Foreign Keys

Use

user_id

order_id

product_id

---

# Timestamps

Recommended

created_at

updated_at

deleted_at (optional)

---

# Data Types

Money

Use:

DECIMAL

Never FLOAT.

Dates

Use timezone-aware timestamps.

Boolean

Prefix with

is_

has_

can_

Examples

is_active

has_access

can_edit

---

# Constraints

Use:

- PRIMARY KEY
- FOREIGN KEY
- UNIQUE
- CHECK
- NOT NULL

Don't rely only on application validation.

---

# Soft Deletes

If supported

deleted_at

Remember every query must ignore deleted rows unless explicitly requested.

---

# Documentation

Document:

- ER diagrams
- Relationships
- Constraints
- Status values
- Enumerations

---

# Checklist

- Naming follows standards
- Foreign keys defined
- Indexes created
- Constraints added
- Documentation updated