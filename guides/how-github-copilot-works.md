# How GitHub Copilot Works (Conceptual Internals + Examples)

## Overview

GitHub Copilot is an AI pair programmer that generates code, explanations, and edits inside your IDE. It works by:

- Collecting **relevant context** from your editor (what you’re editing + nearby/related code).
- Sending a **prompt** (instructions + code context) to a hosted **large language model (LLM)**.
- Receiving multiple candidate completions/edits, then **ranking** and presenting the best one.
- Letting you accept, partially accept, or reject suggestions, creating a tight **human-in-the-loop** loop.

This guide explains the moving parts and the request/response pipeline for:

- **Inline completions** (ghost text)
- **Copilot Chat** (Q&A, refactors, multi-file tasks)
- **Agent-style workflows** (where available)

It also includes practical examples you can paste into code or Chat.

> Note: GitHub doesn’t publish every low-level detail of Copilot’s runtime. The “internals” here are a **conceptual model** that matches how modern LLM coding assistants typically operate. Exact behavior varies by IDE, Copilot version, org policy, and model.

---

## Mental Model: “Context → Prompt → Model → Candidates → Ranking → You”

At a high level:

1. **You type / select / ask** (cursor position, selection, or chat message).
2. The IDE extension gathers **context**.
3. Copilot constructs a **prompt**.
4. The prompt is sent to a **hosted model**.
5. The model returns **one or more candidates**.
6. Copilot applies **post-processing + ranking**.
7. The IDE shows suggestions and you **accept or edit**.

This resembles search + generation:

- Retrieval: “Which files/snippets matter right now?”
- Generation: “Given these constraints and examples, produce the most likely next code.”

---

## Components and Responsibilities

### 1) IDE Extension (VS Code / JetBrains / etc.)

The extension is responsible for:

- Detecting events (typing, new line, trigger completion, chat request).
- Gathering editor context (current file, selection, nearby code, language mode).
- Applying local rules (debouncing, token limits, user/org settings).
- Rendering inline suggestions and managing accept/partial accept.

### 2) Copilot Service (Cloud)

A service layer typically handles:

- Authentication and policy enforcement (consumer vs business/enterprise).
- Request shaping and routing to an appropriate model.
- Safety filtering (before and/or after model output).
- Telemetry/metrics (depending on settings).

### 3) LLM (Code-capable model)

The model:

- Consumes a prompt containing instructions + code context.
- Predicts likely continuations or structured edits.
- Produces one or more candidates.

Models differ in:

- Context window size (how much text they can consider).
- Code quality across languages/frameworks.
- Ability to follow constraints reliably.
- Tool-use / agent capabilities (if enabled).

### 4) Ranking / Post-processing

Before you see output, Copilot may:

- Rank candidates by likelihood and heuristics.
- Prefer suggestions that compile/typecheck (where signals exist).
- Apply formatting or indentation fixes.
- Remove obviously unsafe patterns.

---

## Two Modes: Inline Completions vs Chat

### Inline completions (ghost text)

Inline completion optimizes for:

- **Speed** (low latency)
- **Locality** (current file, nearby code)
- **Short horizon** (what code should come next)

Typical triggers:

- You pause after typing.
- You type a function signature and press Enter.
- You add a comment “implement …” above a stub.

### Chat

Chat optimizes for:

- **Longer instructions** and richer constraints.
- **Explanations** and rationale.
- **Multi-file reasoning** (when allowed by the IDE integration and permissions).

Chat often supports different “shapes” of work:

- Explain code
- Generate tests
- Refactor
- Fix failing build
- Add documentation

---

## Context: What Copilot “Sees”

Copilot can only generate based on what’s included in the prompt.

### Common context sources

- **Current file**: surrounding lines around the cursor.
- **Open tabs / recent files**: likely related code.
- **Project structure signals**: filenames, imports, symbols.
- **Selection** (Chat): highlighted code is usually prioritized.
- **Build/test errors** (Chat): if you paste logs, they become context.

### Why context matters

LLMs are pattern learners. The closer you place a pattern to the cursor, the more likely Copilot will continue it correctly:

- naming conventions
- error handling style
- logging approach
- dependency injection patterns
- test style

### Context limits (the “window”)

Models have a finite context window, so Copilot must choose what to include. If your prompt is huge:

- important details may be truncated
- output may drift or miss constraints

Practical implication:

- Put constraints and examples **near the cursor** (inline) or at the **top of your chat message**.

---

## Prompt Construction (What the Model Receives)

You don’t usually see the exact prompt, but it typically includes:

- System/policy instructions (safety, formatting constraints)
- Your instruction (comment or chat request)
- Code context (surrounding code + relevant snippets)
- “Stop” markers or formatting hints

### Inline example: comment-driven prompt

You type:

```py
# Implement parse_items(text):
# - split on commas
# - trim whitespace
# - ignore empty entries
# - return list[str]

def parse_items(text: str) -> list[str]:

```

The model sees the comment, signature, and nearby code, and predicts a likely implementation.

### Chat example: instruction + constraints

In Chat you might say:

> Refactor this function to remove duplication. Keep behavior identical. Do not change public API. Add unit tests for edge cases.

This explicit constraint framing strongly affects output quality.

---

## Candidate Generation and Ranking

Most assistants don’t rely on a single guess. They can request:

- multiple candidates (“n-best”)
- multiple temperatures (more deterministic vs more creative)

Then they rank candidates using signals like:

- syntactic correctness (indentation/brackets)
- import availability
- type hints / inferred types
- similarity to surrounding style

You experience this as:

- several suggestions when cycling completions
- the top suggestion often matching local conventions

---

## Safety, Privacy, and Policy (Practical View)

Organizations can configure what Copilot is allowed to do. Typical concerns:

- **Secrets**: never paste API keys/tokens into Chat.
- **Sensitive code**: policy may restrict what context is sent.
- **Licensing**: generated code might resemble public patterns.

Practical steps for teams:

- Use secret scanning and pre-commit checks.
- Treat Copilot output like a junior engineer’s draft: review, test, and secure.
- Prefer tests-first to force verifiable behavior.

---

## Examples: Inline Completions (Copy/Paste)

### Example 1: Python utility function

```py
import hashlib

# Implement compute_checksum(data) returning SHA256 hex digest.
# - data can be str or bytes
# - for str, encode as UTF-8
# - raise TypeError for other types

def compute_checksum(data):

```

What to look for in the suggestion:

- correct type branching
- stable encoding choice
- returns `hexdigest()`

### Example 2: JavaScript retry helper

```js
/**
 * Implement fetchWithRetries(url, options)
 * - retry up to 3 times on network errors
 * - exponential backoff starting at 200ms
 * - return parsed JSON
 * - do not add external dependencies
 */
export async function fetchWithRetries(url, options = {}) {}
```

What to look for:

- distinguishes HTTP error vs network error
- waits between retries
- doesn’t swallow the final error

### Example 3: Tests-first prompt (pytest)

```py
# test_parse_items.py

def test_parse_items_empty():
    assert parse_items("") == []

def test_parse_items_trims_and_ignores_empty():
    assert parse_items(" a, ,b ,  c ") == ["a", "b", "c"]

# Copilot: implement parse_items(text) to pass the tests above.
```

Then create `parse_items` under test and let Copilot implement the minimum.

---

## Examples: Copilot Chat (Practical Prompts)

### Explain

Prompt:

> Explain what this function does in 5 bullets. Call out edge cases and time complexity.

### Generate tests

Prompt:

> Write unit tests for this function (pytest). Cover empty input, malformed input, and large input. Keep tests deterministic.

### Refactor without changing behavior

Prompt:

> Refactor to improve readability and remove duplication. Keep behavior identical. Do not rename public functions. Provide the diff.

### Debug from a failing test

Prompt:

> Here is a failing test and stack trace. Identify the root cause and propose a minimal fix. Then suggest one more test that would have caught this earlier.

(Then paste the failing test + stack trace.)

---

## How to Get Better Output (Mechanics-Based Tips)

Because Copilot is driven by local context and constraints, these techniques work reliably:

- Put constraints **next to the code** (inline) or at the **top** (chat).
- Provide 1–2 **examples** of input/output for tricky transformations.
- Use **tests-first** for any non-trivial behavior.
- Explicitly say what **not** to do (no new deps, no API changes, no broad refactors).

---

## Common Failure Modes (and Fixes)

- **Hallucinated APIs**: Copilot invents methods/classes.

  - Fix: paste the real interface or open the file with the definition.

- **Wrong assumptions about data**: e.g., `None` vs empty string.

  - Fix: add tests that define behavior.

- **Over-refactoring**: large, risky diffs.

  - Fix: constrain scope: “Only modify function X. Do not change other files.”

- **Security footguns**: unsafe deserialization, shell injection, weak crypto.
  - Fix: add a security constraint and run linters/scanners.

---

## Quick Glossary

- **Context window**: maximum text the model can consider.
- **Prompt**: the full input the model receives (instructions + context).
- **Completion**: predicted continuation of code.
- **Edit**: model returns a change plan or patch (common in chat/agents).
- **Ranking**: choosing the best candidate suggestion.

---

## Suggested Exercises (Fits This Repo)

- Apply “tests-first” from [labs/prompting-techniques/tests-first-copilot.md](../labs/prompting-techniques/tests-first-copilot.md) to implement a small parser.
- Take an existing function in your repo and ask Chat to add tests only.
- Ask for a refactor with constraints and compare the diff size when constraints are missing vs present.
