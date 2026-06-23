# AI Development Workflow

## Purpose

This document defines how the Sport Intelligence Platform (SIP) is developed using a human-AI team.

The goal is to ensure consistent architecture, high code quality, and efficient collaboration.

---

# Team Roles

## Founder / Product Owner

Responsibilities:

* Define product vision.
* Decide which user problems should be solved.
* Approve new features.

---

## Chief Architect

Responsibilities:

* Maintain architecture consistency.
* Design APIs.
* Review implementations.
* Plan development sprints.
* Approve architectural decisions.

---

## Senior Python Engineer (AI)

Responsibilities:

* Implement features.
* Refactor code.
* Write tests.
* Improve documentation.
* Never redesign the architecture without approval.

---

# Development Workflow

## Step 1

Identify a new user question.

Example:

> What was the average net time?

---

## Step 2

Check whether the question already exists in `questions.md`.

If yes, continue.

If not, add the question first.

---

## Step 3

Check whether the Analysis API already supports this question.

If yes, reuse the existing function.

If not, design a new function.

---

## Step 4

The Senior Python Engineer implements the feature.

Implementation must follow:

* architecture.md
* ai_context.md
* coding standards

---

## Step 5

The Chief Architect performs code review.

Review criteria:

* Architecture
* API consistency
* Readability
* Reuse
* Simplicity

---

## Step 6

The Founder validates the implementation using real data.

If accepted:

* merge into the project
* update documentation if necessary

---

# Golden Rules

* Questions drive the API.
* The API drives the implementation.
* Implementation never drives the product.
* Never duplicate logic.
* Prefer reusable functions.
* Build for long-term maintainability.
