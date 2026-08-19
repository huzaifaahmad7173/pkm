---
title: Component Conventions
description: Guidelines for naming, structuring, and building reusable UI components.
tags:
  - frontend
  - components
  - architecture
status: Draft
related:
  - coding-standards.md
  - project-structure.md
---

# Component Conventions

## Overview

Component conventions provide a consistent way to design and organize UI components across a project. Following the same standards makes components easier to understand, reuse, test, and maintain. These guidelines are framework-agnostic and apply to libraries such as React, Vue, Angular, and Svelte.

---

# Naming

Use descriptive names that reflect the component's purpose rather than its appearance.

Examples:

```
UserCard
ProductGrid
SearchInput
NavigationBar
```

Avoid vague names like `Box`, `Item`, or `Component`.

---

# Structure

Organize components by responsibility and keep related files together.

Example:

```
components/
├── ui/
├── layout/
├── features/
└── shared/
```

A reusable component folder may contain:

```
Button/
├── Button.vue
├── Button.test.ts
├── styles.css
└── README.md
```

---

# Props

Props define a component's public API. Keep them minimal, clearly named, and typed. Provide sensible defaults where appropriate, and never modify props directly inside the component.

---

# Composition

Prefer building complex interfaces from smaller reusable components instead of creating large, monolithic ones. Keep business logic separate from presentation whenever possible.

---

# Lifecycle

Use lifecycle hooks only for tasks such as initialization, data loading, or resource cleanup. Avoid placing large amounts of business logic inside lifecycle methods.

---

# Examples

### Good

```
ProductCard
├── Displays product information
├── Receives props
└── Emits user actions
```

### Poor

```
DashboardComponent
├── Fetches data
├── Handles routing
├── Manages forms
└── Renders UI
```

---

# Anti-Patterns

Avoid:

- Components with multiple responsibilities
- Mutating props
- Duplicated UI instead of reusable components
- Excessive direct DOM manipulation

---

# Checklist

Before merging a component, verify that:

- [ ] The component has a single responsibility.
- [ ] Naming follows project conventions.
- [ ] Props are clear and well defined.
- [ ] The component is reusable where appropriate.
- [ ] Lifecycle hooks are used only when necessary.
- [ ] Documentation and tests are included for shared components.

---

# Key Takeaways

- Keep components small and focused.
- Use consistent naming and structure.
- Design clear and minimal component APIs.
- Prefer composition over large components.
- Keep lifecycle logic simple and maintainable.
