---
title: API Endpoint Catalog
description: A simple list of the API endpoints provided by the backend.
tags:
  - api
  - backend
  - endpoints
status: Draft
---

# API Endpoint Catalog

## Overview

An API Endpoint Catalog is a list of all the endpoints available in the backend.

It helps developers quickly see:

- What endpoints exist.
- What each endpoint does.
- Which HTTP method is used.
- What data is required.
- What the endpoint returns.

---

# Endpoint Format

Use this format for each endpoint:

### `METHOD /path`

- **Purpose:** What it does.
- **Auth:** Public or required.
- **Request:** Data sent to the endpoint.
- **Response:** Data returned by the endpoint.

---

# Examples

### `GET /users`

- **Purpose:** Get all users.
- **Auth:** Required.
- **Request:** None.
- **Response:** List of users.

### `GET /users/{id}`

- **Purpose:** Get one user.
- **Auth:** Required.
- **Request:** User ID.
- **Response:** User information.

### `POST /users`

- **Purpose:** Create a user.
- **Auth:** Required.
- **Request:** User information.
- **Response:** Created user.

### `PUT /users/{id}`

- **Purpose:** Update a user.
- **Auth:** Required.
- **Request:** User ID and updated data.
- **Response:** Updated user.

### `DELETE /users/{id}`

- **Purpose:** Delete a user.
- **Auth:** Required.
- **Request:** User ID.
- **Response:** Success message.

---

# Endpoint List

## Users

- `GET /users` — Get users.
- `GET /users/{id}` — Get one user.
- `POST /users` — Create a user.
- `PUT /users/{id}` — Update a user.
- `DELETE /users/{id}` — Delete a user.

## Authentication

- `POST /auth/login` — Login.
- `POST /auth/register` — Register.
- `POST /auth/logout` — Logout.

---

# Rules

- Add every new endpoint to the catalog.
- Use clear endpoint names.
- Document what each endpoint does.
- Keep the catalog updated when endpoints change.