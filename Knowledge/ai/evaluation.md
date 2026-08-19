---
title: AI Evaluation
description: How to test and measure the quality of AI features.
tags:
  - ai
  - evaluation
  - testing
status: Draft
---

# AI Evaluation

## Overview

AI evaluation checks whether an AI feature produces useful and correct results.

AI output can change when the model, prompt, or data changes, so features should be tested regularly.

---

# Evaluation Set

An evaluation set is a collection of example inputs used to test an AI feature.

Include:

- Normal inputs
- Edge cases
- Invalid inputs
- Long inputs
- Difficult examples
- Previously reported failures

Store evaluation cases in the project repository.

---

# Evaluation Criteria

Different AI features require different measurements.

Examples:

- Accuracy
- Relevance
- Correctness
- Completeness
- Format correctness
- Safety

---

# Running Evaluations

Run evaluations when:

- The model changes.
- The prompt changes.
- The output format changes.
- Important application logic changes.

---

# Regression Testing

When an AI feature produces a bad result:

1. Add the example to the evaluation set.
2. Run the evaluation.
3. Fix the prompt, model, or code.
4. Run the evaluation again.
5. Make sure previous cases still pass.

---

# Best Practices

- Keep evaluation cases in version control.
- Test realistic examples.
- Track evaluation results.
- Add failed cases to the test set.
- Define a minimum quality score.