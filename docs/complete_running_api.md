# Complete Running API

## Purpose

The Complete Running API defines every question that the Sport Intelligence Platform should eventually answer about runners, races, and performance.

The API is designed from the user's perspective.

Every public function should exist because it answers a meaningful user question.

---

## API Domains

- Runner API
- Race API
- Statistics API
- Comparison API
- Insights API

---

# Runner API

## Purpose

The Runner API answers questions about a single runner.

### User Questions

#### Identity

- What is my bib number?
- What is my name?
- Which city am I from?
- Which country am I from?
- Which team did I represent?

#### Performance

- What was my net time?
- What was my gun time?
- What was my average pace?

#### Ranking

- What place did I finish overall?
- What place did I finish in my gender category?
- What category did I compete in?

#### Splits

- What was my 5K split?
- What was my 10K split?
- What was my 15K split?
- What was my 20K split?

---

# Race API

## Purpose

The Race API answers questions about the entire race.

### User Questions

#### Participation

- How many runners finished the race?
- How many runners started the race?
- How many runners did not finish?

#### Performance

- What was the fastest finish time?
- What was the slowest finish time?
- What was the average finish time?
- What was the median finish time?

#### Demographics

- How many women finished?
- How many men finished?
- How many countries were represented?
- Which country had the most runners?

#### Rankings

- Who won the race?
- Who was the fastest woman?
- Who was the fastest man?

---

# Statistics API

## Purpose

The Statistics API provides statistical information about race results.

### User Questions

- What is the average finish time?
- What is the median finish time?
- What is the fastest finish time?
- What is the slowest finish time?
- What is the time distribution?
- What is the standard deviation?
- What is the 10th percentile?
- What is the 25th percentile?
- What is the 50th percentile?
- What is the 75th percentile?
- What is the 90th percentile?

---

# Comparison API

## Purpose

The Comparison API compares runners, groups and races.

### User Questions

- How do I compare with another runner?
- How do I compare with my age category?
- How do I compare with my gender?
- How do I compare with runners from my country?
- How does this race compare with another race?
- How has my performance changed over time?

---

# Insights API

## Purpose

The Insights API generates evidence-based insights from race data.

### User Questions

- Why was this my fastest race?
- Why was this my slowest race?
- Did I start too fast?
- Did I finish strongly?
- Did I run a negative split?
- Was my pacing consistent?
- What was my strongest section?
- What was my weakest section?
- What should I improve before my next race?
- What story does this race tell?