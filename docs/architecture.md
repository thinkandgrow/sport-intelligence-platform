# Sport Intelligence Platform (SIP)

## Vision

Sport Intelligence Platform (SIP) is a long-term research platform for sports analytics.

The goal is not only to analyze data but to build reusable tools that transform raw sports data into reliable knowledge.

---

## Core Principles

### 1. Domain-first architecture

Code is organized by sports domains.

Examples:

- Running
- Football
- Baseball

---

### 2. One function, one responsibility

Every function should answer one research question.

---

### 3. Reusable production code

Reusable code belongs in `src/`.

---

### 4. Exploration belongs in notebooks

Experiments, visualizations and prototypes belong in `notebooks/`.

---

### 5. Thin scripts

Scripts orchestrate work.

Business logic belongs inside the library.

---

### 6. Raw data is immutable

Raw datasets are never modified.

Processed datasets are stored separately.

---

### 7. Continuous improvement

The platform evolves through small, well-tested improvements following the Kaizen philosophy.