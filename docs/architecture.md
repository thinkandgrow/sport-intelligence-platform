# Sport Intelligence Platform (SIP)

## Architecture Principles

### Vision

Sport Intelligence Platform is not a collection of scripts.

It is an analytics engine that answers questions about sports data.

The long-term goal is to allow users to ask questions in natural language while the platform translates them into analytical operations.

---

## Architecture Layers

```
User
    │
    ▼
Natural Language
    │
    ▼
Question Interpreter
    │
    ▼
Analysis API
    │
    ▼
Pandas Engine
    │
    ▼
Race Data
```

---

## Responsibilities

### Race Data

Stores raw race results.

### Pandas Engine

Provides efficient dataframe operations.

### Analysis API

Contains reusable domain-specific analytical functions.

Examples:

* mean_net_time()
* median_net_time()
* fastest_runner()
* slowest_runner()

The Analysis API is the only layer allowed to interact directly with Pandas.

### Question Interpreter

Translates user questions into calls to the Analysis API.

Example:

Question:

> What was the average net time?

↓

Function:

mean_net_time(df)

---

## Design Principles

* Keep functions pure.
* Keep functions small.
* Prefer readability over cleverness.
* Do not duplicate logic.
* Use English names.
* Separate analysis from presentation.
* Every function should answer one analytical question.

---

## Long-Term Goal

Chat Your Race should never execute raw Pandas operations directly.

Every user question should be translated into a reusable function from the Analysis API.
