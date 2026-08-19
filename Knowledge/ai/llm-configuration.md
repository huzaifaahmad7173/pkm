---
title: LLM Configuration
description: Basic guidelines for configuring and using language models in the application.
tags:
  - ai
  - llm
  - configuration
status: Draft
---

# LLM Configuration

## Overview

LLM configuration defines how the application connects to and uses a language model. It includes the model, API settings, and basic generation settings.

---

# Model

Choose the model based on the task.

```text
Model: llama3.2
```

Different models may provide different levels of speed, cost, and quality.

---

# Provider

The provider supplies the language model.

Examples:

- Ollama
- OpenAI
- Google Gemini
- Anthropic

Keep the provider configuration separate from application logic when possible.

---

# API Configuration

Store API settings securely.

```text
LLM_PROVIDER=ollama
LLM_MODEL=llama3.2
```

Never place API keys directly in source code.

---

# Generation Settings

Common settings include:

- **Temperature** → Controls how creative the response is.
- **Max tokens** → Limits the response length.
- **Top P** → Controls the range of possible responses.

Use lower randomness for tasks that require consistent answers.

---

# System Prompt

A system prompt defines the general behavior of the model.

```text
You are a helpful coding assistant.
Follow the project's coding standards.
```

Keep system prompts clear and focused.

---

# Best Practices

- Keep model configuration centralized.
- Store secrets in environment variables.
- Use the appropriate model for each task.
- Keep generation settings consistent.
- Test configuration changes before production.

---

# Key Takeaways

- Define the model and provider clearly.
- Keep API keys out of source code.
- Configure generation settings carefully.
- Keep LLM configuration separate from application logic.