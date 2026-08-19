---
title: API Design Standards
description: Simple rules for designing consistent and easy-to-use APIs.
tags:
  - api
  - backend
  - design
status: Draft
---

# API Design Standards

## Overview

API design standards are rules that help keep all API endpoints consistent, clear, and easy to use.

The same naming, HTTP methods, responses, and error handling should be used throughout the project.

---

# URL Naming

Use nouns for resources.

Good:

```text
/users
/products
/orders
```

Avoid:

```text
/getUsers
/createProduct
/deleteOrder
```

Use plural names for collections.

---

# HTTP Methods

Use HTTP methods according to their purpose.

| Method | Purpose |
|---|---|
| GET | Get data |
| POST | Create data |
| PUT | Replace data |
| PATCH | Update part of data |
| DELETE | Delete data |

---

# URL Parameters

Use IDs to identify specific resources.

Example:

```text
GET /users/123
GET /products/45
```

Use query parameters for filtering, searching, sorting, and pagination.

Example:

```text
GET /users?limit=10
GET /products?search=phone
```

---

# Request and Response

Use a consistent format for requests and responses.

Example request:

```json
{
  "name": "Ali",
  "email": "ali@example.com"
}
```

Example response:

```json
{
  "id": 1,
  "name": "Ali",
  "email": "ali@example.com"
}
```

---

# Status Codes

Use the correct HTTP status code.

| Code | Meaning |
|---|---|
| 200 | Success |
| 201 | Created |
| 204 | Success with no content |
| 400 | Invalid request |
| 401 | Not authenticated |
| 403 | Not allowed |
| 404 | Not found |
| 409 | Conflict |
| 500 | Server error |

---

# Error Responses

Return errors in a consistent format.

Example:

```json
{
  "error": {
    "code": "USER_NOT_FOUND",
    "message": "User not found"
  }
}
```

Do not expose sensitive internal errors to clients.

---

# Authentication

Protected endpoints should require authentication.

Example:

```text
Authorization: Bearer <token>
```

Authentication requirements should be documented for every protected endpoint.

---

# Pagination

Use pagination when returning large amounts of data.

Example:

```text
GET /users?limit=20&offset=0
```

This prevents the API from returning too much data at once.

---

# Best Practices

- Use clear and consistent URLs.
- Use HTTP methods correctly.
- Use appropriate status codes.
- Keep request and response formats consistent.
- Validate incoming data.
- Protect authenticated endpoints.
- Return clear error messages.
- Do not expose sensitive information.
- Document every endpoint.
- Keep the API design consistent across the project.

---

# Key Takeaways

- Use nouns in URLs.
- Use HTTP methods for actions.
- Use consistent responses.
- Use correct status codes.
- Validate requests.
- Document endpoints.
- Keep the API simple and predictable.