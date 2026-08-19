---
title: Project Structure
description: Guidelines for organizing folders, naming files, and managing shared code.
tags:
  - frontend
  - project-structure
status: Draft
related:
  - component-conventions.md
  - coding-standards.md
---

# Project Structure

## Overview

A clear project structure makes the codebase easier to navigate, maintain, and scale. Keeping files organized helps developers quickly find code and reduces duplication.

---

# Folder Organization

Group files by their purpose.

**Example**

```text
src/
├── assets/
├── components/
├── layouts/
├── pages/
├── services/
├── styles/
├── utils/
└── stores/
```

**Guidelines**

- Keep similar files together.
- Avoid unnecessary nesting.
- Organize folders consistently.

---

# Naming Conventions

Use descriptive names for files and folders.

**Examples**

```text
UserCard.vue
ProductList.vue
AuthService.js
```

Avoid names like:

```text
File.vue
Temp.js
Test.vue
```

---

# Feature Organization

For larger projects, group related files into feature folders.

**Example**

```text
features/
├── auth/
├── products/
└── dashboard/
```

Each feature can contain its own components, pages, and services.

---

# Shared Code

Place reusable code in shared folders instead of duplicating it.

Examples include:

- Components
- Utilities
- Services
- Styles

---

# Best Practices

- Keep the folder structure simple.
- Use consistent naming.
- Reuse shared code.
- Remove unused files regularly.

---

# Key Takeaways

- Organize files by purpose or feature.
- Use clear and consistent names.
- Keep reusable code in shared folders.
- Maintain a simple and organized project structure.