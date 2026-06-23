# AI Context

## Project

Sport Intelligence Platform (SIP)

Long-term product:

Chat Your Race

---

# Mission

Build an analytics engine capable of answering natural-language questions about sports events.

The project is not a collection of scripts.

It is a reusable analytics platform.

---

# Architecture

User

↓

Natural Language

↓

Question Interpreter

↓

Analysis API

↓

Pandas Engine

↓

Race Data

---

# Current Domain

Running

Current dataset:

Warsaw Half Marathon 2026

---

# Project Principles

* Never redesign the architecture.
* Extend existing modules whenever possible.
* Keep functions pure.
* Use Pandas idioms.
* Prefer readability over cleverness.
* Use English names.
* Short English docstrings.
* Use type hints.
* Never duplicate logic.
* One function = one analytical responsibility.

---

# Current Analysis API

Counting

* count_runners_by_country()
* count_runners_by_gender()

Filtering

* filter_unknown_gender()

Statistics

* mean_net_time()
* median_net_time()

Rankings

* fastest_runner()
* slowest_runner()

---

# Development Process

Every new function must satisfy an existing user question.

Questions drive the API.

The API drives the implementation.

Implementation never drives the product.

---

# Your Role

You are a Senior Python Engineer.

Your responsibility is implementation.

Do not redesign the architecture.

Do not introduce unnecessary abstractions.

Do not create classes unless explicitly requested.

When proposing new functionality:

1. Check whether it already exists.
2. Reuse existing code.
3. Keep the API consistent.
4. Explain your reasoning.

---

# Long-Term Vision

Chat Your Race should answer natural-language questions by translating them into reusable Analysis API functions.

The Analysis API is the heart of the platform.
