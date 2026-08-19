---
title: API Versioning
description: Guidelines for managing different versions of the backend API.
tags:
  - backend
  - api
  - versioning
status: Draft
related:
  - api-overview.md
  - request-response.md
---

# API Versioning

## Overview

API versioning allows the backend to change without breaking applications that still use the older API.

For example:

```text
/api/v1/users
/api/v2/users
```

Here, `v1` and `v2` are different versions of the same API.

---

# When to Create a New Version

Create a new version when a change can break existing clients.

Examples:

- Removing an endpoint.
- Renaming a field.
- Changing the data format.
- Changing how an endpoint works.

Small bug fixes and backward-compatible changes usually do not need a new version.

---

# Versioning Rules

- Use simple versions such as `v1`, `v2`, and `v3`.
- Keep the version in the API URL.
- Document important changes.
- Keep older versions working when necessary.
- Remove old versions only after clients have migrated.

---

# Example

```text
/api/v1/products
/api/v2/products
```

`v1` can continue working while clients move to `v2`.

---

# Best Practices

- Avoid creating versions unnecessarily.
- Keep each version consistent.
- Clearly document breaking changes.
- Test each API version before deployment.

---

# Key Takeaways

- API versioning prevents breaking existing clients.
- Use `v1`, `v2`, etc. to identify versions.
- Create a new version for breaking changes.
- Keep versioning simple and consistent.