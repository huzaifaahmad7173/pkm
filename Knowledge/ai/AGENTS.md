# AI Agents Guide

Rules for working on AI/LLM features. Source of truth: the docs in this folder (`llm-configuration.md`, `model-notes.md`, `versioning.md`, `error-handling.md`, `evaluation.md`, `llm-monitoring.md`).

## Configuration

- Keep model + provider config centralized (env vars or one config file): `LLM_PROVIDER`, `LLM_MODEL`.
- Never put API keys or secrets in source code — use environment variables / secret manager.
- Keep provider configuration separate from application logic.
- Set generation settings deliberately: temperature (creativity), max tokens (length), top P (range). Lower randomness for tasks needing consistent answers.
- Write clear, focused system prompts.

## Model Selection & Versioning

- Choose models per feature based on quality, accuracy, cost, speed, context size, privacy, reliability. The best model isn't always the newest/largest.
- Test models against the project's evaluation set before switching; compare quality and cost; document why a model was selected.
- Keep the model name in one place; never hardcode it across the app.
- Record model changes (previous → new → reason). Keep the previous working model available for rollback.
- Reuse initialized models; avoid changing models without testing.

## Error Handling

- Expect failures: invalid input, model unavailable, API failures, timeouts, rate limits, invalid responses, token/context limits.
- Validate input before sending to the model. Set reasonable timeouts.
- Retry only temporary failures (network, timeout, 429/rate limit, transient unavailability). Do not retry invalid requests.
- Use a fallback model, then a user-friendly error, when the primary service is unavailable.
- Keep user-facing messages simple; log technical detail (error type, request ID, model, timestamp, reason) for developers.
- Never log passwords, API keys, tokens, or sensitive user data.

## Evaluation

- Maintain an evaluation set in version control covering normal, edge, invalid, long, and previously failed inputs.
- Define criteria per feature (accuracy, relevance, correctness, completeness, format, safety) and a minimum quality score.
- Run evaluations when the model, prompt, output format, or relevant app logic changes.
- Regression flow: add the bad case → run eval → fix prompt/model/code → rerun → ensure prior cases still pass.
- Track evaluation results over time.

## Monitoring

- Monitor response time, error rate, request count, token usage, model usage, and user feedback.
- Track AI-specific errors (model unavailable, timeout, invalid response, rate limit, API failure).
- Logs must contain enough to debug without exposing sensitive data.
