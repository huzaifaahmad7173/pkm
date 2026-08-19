---
title: API Technologies
description: Technologies used to build and support the backend API.
tags:
  - backend
  - api
  - technology
status: Draft
---

# API Technologies

## Overview

This document lists the main technologies used to build the project's API and explains the purpose of each one.

---

# Python

## Purpose

Python is the main programming language used to build the backend.

**Used for:**

- Backend logic
- Data processing
- API functionality
- Database operations

---

# FastAPI

## Purpose

FastAPI is the main framework used to build the API.

**Used for:**

- Creating API endpoints
- Handling requests
- Validating data
- Authentication
- API documentation

---

# SQLite

## Purpose

SQLite is used as the database for storing application data.

**Used for:**

- Storing data
- Reading data
- Updating data
- Deleting data

---

# Pydantic

## Purpose

Pydantic is used by FastAPI to validate and structure API data.

**Used for:**

- Request validation
- Response validation
- Data models
- Type checking

---

# SQLAlchemy

## Purpose

SQLAlchemy is used to communicate with the SQLite database using Python.

**Used for:**

- Database models
- Database queries
- Creating and updating records
- Managing database connections

---

# JSON

## Purpose

JSON is the main format used to exchange data between the frontend and API.

Example:

```json
{
  "name": "John",
  "email": "john@example.com"
}
```

---

# REST API

## Purpose

The API follows REST principles to organize endpoints around resources.

Example:

```text
GET    /api/users
POST   /api/users
GET    /api/users/1
PUT    /api/users/1
DELETE /api/users/1
```

---

# Key Takeaways

- **Python** → Backend programming language.
- **FastAPI** → API framework.
- **Pydantic** → Data validation.
- **SQLAlchemy** → Database interaction.
- **SQLite** → Database.
- **JSON** → Data exchange format.
- **REST** → API design approach.