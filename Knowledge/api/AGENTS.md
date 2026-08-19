# API Agents Guide

Rules for working with the backend API. Source of truth: the docs in this folder (`api-overview.md`, `design-standards.md`, `endpoint-catalog.md`, `request-response.md`, `versioning.md`, `performance.md`, `technologies.md`).

## Stack

- **Python** is the backend language.
- **FastAPI** is the API framework (endpoints, request validation, auth, auto-docs).
- **Pydantic** for request/response validation and data models.
- **SQLAlchemy** for database interaction (SQLite).
- **JSON** is the data exchange format.
- API follows **REST** principles with resource-based endpoints.

## URL & Method Conventions

- Use nouns (plural) for resources: `/users`, `/products`, `/orders`. Never verb-style paths (`/getUsers`).
- Map HTTP methods by purpose: GET read, POST create, PUT replace, PATCH partial update, DELETE remove.
- Use path params for a specific resource (`GET /users/123`); use query params for filtering, search, sort, pagination.
- Endpoints are versioned in the URL (`/api/v1/users`). Create a new version only for breaking changes; keep old versions working until clients migrate.

## Request & Response

- Use a consistent structure on every endpoint. Success envelope: `{ "success": true, "data": ... }`. Error envelope: `{ "success": false, "message": "..." }`.
- Use standard HTTP status codes (200, 201, 204, 400, 401, 403, 404, 409, 500).
- Return errors in a consistent shape: `{ "error": { "code": "...", "message": "..." } }`. Never expose sensitive internal errors.
- Validate incoming data before processing (Pydantic).
- Paginate large results (`?limit=20&offset=0` or `?page=1&limit=20`).

## Security & Performance

- Protect sensitive endpoints with auth: `Authorization: Bearer <token>`. Document auth requirements per endpoint.
- Keep responses small: return only required fields, avoid heavy nesting, compress when appropriate.
- Use efficient DB queries and indexes; cache frequently requested, rarely changing data.
- Apply rate limiting to prevent abuse and protect expensive endpoints.
- Monitor slow endpoints and optimize them.

## Documentation

- Every endpoint must be documented in the endpoint catalog (`endpoint-catalog.md`) using: `METHOD /path`, Purpose, Auth, Request, Response.
- Keep the catalog updated whenever endpoints change.
