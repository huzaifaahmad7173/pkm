---
title: State Management
description: Guidelines for managing local, shared, global, server, and URL state in frontend applications.
tags:
  - frontend
  - state-management
  - architecture
status: Draft
related:
  - component-conventions.md
  - technologies.md
  - coding-standards.md
---

# State Management

## Overview

State management defines how application data is stored, updated, and shared between components. Choosing the appropriate type of state keeps applications predictable, maintainable, and easier to debug. As a general rule, keep state as close as possible to where it is used and only share it when necessary.

---

# Local State

## Purpose

Local state belongs to a single component and is not needed elsewhere. It is ideal for temporary UI data and component-specific behavior.

**Use for**

- Form inputs
- Modal visibility
- Dropdown menus
- Loading indicators
- Selected tabs

**Guidelines**

- Keep state inside the component.
- Do not move it to a global store unless multiple components require it.

---

# Shared State

## Purpose

Shared state is used by a small group of related components.

**Use for**

- Parent-child communication
- Shared filters
- Wizard or multi-step forms
- Feature-specific data

**Guidelines**

- Lift state to the nearest common parent.
- Avoid unnecessary prop drilling.

---

# Global State

## Purpose

Global state is shared across many parts of the application and persists throughout the user's session.

**Use for**

- Authentication
- User profile
- Theme preferences
- Application settings

**Guidelines**

- Store only truly global data.
- Avoid placing temporary UI state in the global store.

---

# Server State

## Purpose

Server state is data retrieved from an API or backend service.

**Use for**

- API responses
- User data
- Product lists
- Dashboard statistics

**Guidelines**

- Treat the server as the source of truth.
- Cache data when appropriate.
- Refresh stale data when needed.

---

# URL State

## Purpose

URL state stores information in the browser's address bar, allowing users to share or bookmark the current view.

**Use for**

- Search queries
- Filters
- Sorting
- Pagination
- Active tabs

**Guidelines**

- Keep URLs meaningful and readable.
- Store only information that should be shareable.

---

# Best Practices

- Keep state as local as possible.
- Share state only when multiple components need it.
- Use global state sparingly.
- Separate server data from UI state.
- Use the URL for shareable application state.

---

# Key Takeaways

- **Local State** → Component-specific UI.
- **Shared State** → Related components.
- **Global State** → Application-wide data.
- **Server State** → Data from APIs.
- **URL State** → Shareable page state.