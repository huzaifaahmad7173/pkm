# Frontend Agents Guide

Rules for working on the frontend. Source of truth: the docs in this folder (`frontend-technologies.md`, `structure.md`, `conventions.md`, `state-management.md`, `styling.md`, `data-fetching.md`).

## Stack

- **Vue.js** (primary framework): use the Composition API, build reusable, single-responsibility components.
- **Nuxt**: routing, layouts, SSR/SSG, auto-imports. Follow Nuxt's directory structure; keep pages lightweight; put shared logic in composables.
- **Bootstrap**: responsive grid + utility classes before custom CSS. Never edit Bootstrap source files.
- **HTML5 / CSS3 / JavaScript (ES6+)**: semantic markup, accessible, small reusable functions, no globals.

## Project Structure

- Group files by purpose or by feature: `assets/ components/ layouts/ pages/ services/ styles/ utils/ stores/`, or `features/<feature>/`.
- Keep it simple, avoid deep nesting, keep similar files together.
- Put reusable code (components, utils, services, styles) in shared folders. Remove unused files.

## Components

- Name components by purpose, not appearance: `UserCard`, `ProductGrid`, `SearchInput`. Avoid `Box`, `Item`.
- Keep props minimal, typed, with sensible defaults; never mutate props.
- Prefer composition of small components over large monolithic ones; keep business logic separate from presentation.
- Use lifecycle hooks only for init, data loading, or cleanup.
- Organize a reusable component folder with its test and styles (e.g. `Button/Button.vue`, `Button.test.ts`, `styles.css`).
- Before merging: single responsibility, clear naming/props, reusable, docs + tests for shared components.

## State Management

Keep state as close to its use as possible; only share when needed.

- **Local state** → form inputs, modal/dropdown visibility, loading, tabs. Keep inside the component.
- **Shared state** → lift to nearest common parent; avoid prop drilling.
- **Global state** → auth, user profile, theme, settings only.
- **Server state** → treat the API as source of truth; cache and refresh stale data.
- **URL state** → search, filters, sort, pagination; keep URLs readable and shareable.

## Styling

- Keep CSS modular and component-focused; reuse utility classes; avoid duplicate/unused styles and overly specific selectors.
- Use design tokens for colors, spacing, typography, radius, shadows — no hardcoded values.
- Mobile-first responsive design with flexible units; test common screen sizes.
- Support theming (light/dark) via tokens; never hardcode theme colors in components.
- Accessibility: sufficient contrast, visible focus states, don't rely on color alone.

## Data Fetching

- Route all API calls through a centralized API layer, not inside components. Group related functions; reuse instead of duplicating.
- Always show loading states; handle network/server errors with user-friendly messages and retry where appropriate.
- Cache and reuse fetched data; refresh stale data; avoid repeated requests.
- Paginate large datasets; preserve the current page.
- Fetch only when needed; cancel requests when leaving a page.
