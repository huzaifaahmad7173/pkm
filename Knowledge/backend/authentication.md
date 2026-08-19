# Authentication

How users prove who they are, and how the server keeps them signed in.

## Recommended Baseline

- Password hashing with a slow, salted algorithm (argon2id or bcrypt). Never store plain text or MD5/SHA.
- Sessions or tokens, never store credentials client-side beyond the token itself.
- HTTPS everywhere; cookies marked `HttpOnly`, `Secure`, `SameSite`.
- Rate-limit login endpoints (per IP and per account) to slow brute force.
- Standard account-lockout or exponential backoff after repeated failures.

## Session vs Token

| Aspect        | Server session                        | Token (JWT-style)             |
| ------------- | ------------------------------------- | ----------------------------- |
| Storage       | Session store (DB/Redis) + cookie     | Signed token, often in header |
| Revocation    | Immediate (delete session)            | Hard; needs short expiry      |
| Scale-out     | Shared session store needed           | Stateless, easy               |
| Leak risk     | Cookie theft still possible           | Token in every request        |

Pick one and document it; do not mix both for the same auth flow.

## Token Rules

- Short-lived access tokens (15 min) + refresh token that is revocable.
- Include only non-sensitive claims (no passwords, no personal data).
- Validate signature, expiry, issuer, and audience on every request.
- Store tokens in memory/secure storage client-side; never in localStorage if XSS is a concern.

## Multi-Factor & Identity

- Offer TOTP (authenticator apps) or passkeys when feasible.
- Centralize identity decisions: if using an IdP (Auth0, Cognito, Keycloak), all apps go through it.

## Fill In Per Project

- [ ] Auth mechanism in use (sessions, JWT, OAuth/OIDC, passkeys)
- [ ] Password policy (length, rules) and hashing algorithm
- [ ] Login flow diagram/link
- [ ] Password reset flow and expiry
