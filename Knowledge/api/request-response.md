---
title: Request and Response
description: Guidelines for structuring API requests and responses consistently across the application.
tags:
  - backend
  - api
  - request-response
status: Draft
related:
  - api-overview.md
  - authentication.md
---

# Request and Response

## Overview

Requests and responses define how the frontend and backend exchange data. Using a consistent structure makes the API easier to understand, maintain, and integrate.

---

# Request

A request is sent by the client to perform an operation on the server.

A request may include:

- HTTP method
- Endpoint (URL)
- Headers
- Query parameters (optional)
- Request body (optional)

**Example**

```http
POST /api/users
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com"
}
```

---

# Response

A response is returned by the server after processing a request.

A response should include:

- Status code
- Response data (if successful)
- Error message (if unsuccessful)

**Success Example**

```json
{
  "success": true,
  "data": {
    "id": 1,
    "name": "John Doe"
  }
}
```

**Error Example**

```json
{
  "success": false,
  "message": "User not found."
}
```

---

# Status Codes

Use standard HTTP status codes to indicate the result of a request.

| Code | Meaning |
|------|---------|
| 200 | Request successful |
| 201 | Resource created |
| 400 | Invalid request |
| 401 | Unauthorized |
| 404 | Resource not found |
| 500 | Internal server error |

---

# Best Practices

- Use a consistent request format.
- Return consistent response structures.
- Include meaningful error messages.
- Use appropriate HTTP status codes.
- Validate request data before processing.

---

# Key Takeaways

- Requests send data to the server.
- Responses return data or error information.
- Follow a consistent structure for all endpoints.
- Use standard HTTP status codes.