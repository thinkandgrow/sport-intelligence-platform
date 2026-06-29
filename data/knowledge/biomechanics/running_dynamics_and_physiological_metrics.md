# Running Dynamics & Physiological Metrics

---
Version: 1.0

Status: Active

Category: Biomechanics

Knowledge Base: Sport Intelligence Platform

Last Updated: 2026-06-28

Purpose:
Build the knowledge required for the Performance Intelligence Engine.

Reviewed: No

Source Quality:
★★★★★

Used in SIP:
Planned

Related Documents:
- Toyota Kata
- Toyota Way
- Science of Running
---

# Why It Matters

Ten dokument opisuje najważniejsze metryki biomechaniczne i fizjologiczne wykorzystywane do oceny jakości biegu, ekonomii ruchu, zmęczenia, regeneracji oraz ryzyka kontuzji.

Nie jest to dokument o urządzeniach Garmin.

Jest to dokument opisujący wiedzę o człowieku i jego ruchu.

Sport Intelligence Platform wykorzysta te metryki do budowy **Performance Intelligence Engine**, którego celem będzie nie tylko prezentacja danych, ale przede wszystkim ich interpretacja oraz generowanie praktycznych rekomendacji dla zawodników i trenerów.

---

# Category 1 – Running Mechanics

## Purpose

Opisanie sposobu, w jaki zawodnik porusza się podczas biegu.

Running Mechanics odpowiada na pytanie:

> **Jak zawodnik biegnie?**

---

## Cadence

### Definition

Liczba kroków wykonywanych w ciągu jednej minuty (spm).

### Importance

Kadencja opisuje rytm biegu.

Nie istnieje jedna idealna wartość.

Optymalna kadencja zależy od:

- wzrostu
- długości nóg
- prędkości
- techniki
- doświadczenia

### Interpretation

Wyższa kadencja często oznacza:

- krótszy kontakt z podłożem
- mniejsze siły hamujące
- lepszą ekonomię biegu

Najważniejsza jest jednak stabilność oraz naturalny rytm.

### Training Application

Kadencję warto analizować przy tym samym tempie.

Jeżeli przy identycznym tempie kadencja rośnie, a koszt energetyczny pozostaje podobny, może to oznaczać poprawę techniki.

### Possible SIP Insights

- Kadencja pozostaje stabilna przez cały bieg.
- Kadencja spada po 16 km.
- Wzrost kadencji sugeruje poprawę ekonomii biegu.

---

## Stride Length

### Definition

Odległość pomiędzy kolejnymi krokami.

### Importance

Prędkość biegu wynika z połączenia:

- Cadence
- Stride Length

### Interpretation

Długość kroku powinna wynikać z efektywnego odbicia, a nie z nadmiernego wykroku przed środkiem ciężkości.

### Possible SIP Insights

- Długość kroku wzrasta wraz z prędkością.
- Nadmierne wydłużanie kroku może obniżać ekonomię biegu.

---

## Ground Contact Time (GCT)

### Definition

Czas kontaktu stopy z podłożem podczas jednego kroku.

Jednostka:

**ms**

### Importance

Ground Contact Time opisuje sprężystość oraz dynamikę biegu.

### Interpretation

Najlepiej analizować GCT przy identycznym tempie.

Trend jest ważniejszy od pojedynczego pomiaru.

### Training Application

Poprawa GCT może świadczyć o:

- poprawie techniki
- większej sile
- lepszej ekonomii

### Possible SIP Insights

- Ground Contact Time wzrósł o 14% po 17 km.
- GCT skrócił się o 18 ms.
- Zawodnik poprawił ekonomikę biegu.

---

## Ground Contact Time Balance

### Definition

Procentowy udział czasu kontaktu lewej i prawej stopy z podłożem.

### Importance

Opisuje symetrię biegu.

### Interpretation

Długotrwała asymetria może sugerować:

- przeciążenie
- osłabienie jednej strony
- ryzyko kontuzji

### Possible SIP Insights

- Asymetria utrzymuje się od trzech tygodni.
- Zalecana analiza fizjoterapeutyczna.
- Symetria poprawia się wraz z treningiem.

---

## Vertical Oscillation

### Definition

Pionowy ruch środka ciężkości podczas biegu.

### Importance

Każdy dodatkowy centymetr ruchu pionowego oznacza energię niewykorzystaną do ruchu do przodu.

### Possible SIP Insights

- Nadmierna oscylacja obniża ekonomię biegu.
- Oscylacja maleje wraz ze wzrostem kadencji.

---

## Vertical Ratio

### Definition

Relacja pomiędzy Vertical Oscillation a Stride Length.

### Importance

Opisuje efektywność ruchu.

Niższy wskaźnik oznacza lepszą ekonomikę.

### Possible SIP Insights

- Vertical Ratio poprawił się o 6%.
- Zawodnik efektywniej wykorzystuje energię.

---

## Running Power

### Definition

Szacowana moc generowana podczas biegu.

Jednostka:

**Wat**

### Importance

Running Power opisuje rzeczywisty wysiłek niezależnie od profilu trasy.

### Possible SIP Insights

- Moc pozostaje stabilna mimo zmian tempa.
- Spadek mocy wskazuje na narastające zmęczenie.

---

# Category 2 – Physiology

## Purpose

Opisanie reakcji organizmu na wysiłek.

---

## Heart Rate

### Importance

Podstawowa informacja o intensywności wysiłku.

### Possible SIP Insights

- Tętno pozostaje stabilne.
- Występuje dryf tętna.

---

## HRV

### Importance

Opisuje stan regeneracji układu nerwowego.

### Possible SIP Insights

- Spadek HRV sugeruje zmęczenie.
- HRV wróciło do poziomu bazowego.

---

## VO₂ Max

### Importance

Szacunkowa wydolność tlenowa.

### Possible SIP Insights

- Trend VO₂ Max pozostaje wzrostowy.
- Adaptacja treningowa przebiega prawidłowo.

---

## Lactate Threshold

### Importance

Najważniejszy parametr dla biegów długodystansowych.

### Possible SIP Insights

- Tempo progowe wzrosło.
- Próg mleczanowy przesunął się na wyższą intensywność.

---

# Category 3 – Training Intelligence

## Purpose

Opis procesu przygotowań zawodnika.

### Metrics

- Training Load
- Training Status
- Training Readiness
- Recovery Time

### Possible SIP Insights

- Obciążenie treningowe pozostaje zrównoważone.
- Organizm wymaga regeneracji.
- Trening jest produktywny.
- Wzrasta ryzyko przetrenowania.

---

# Category 4 – Race Intelligence

## Purpose

Opis zachowania zawodnika podczas zawodów.

### Metrics

- Pace Strategy
- Race Predictor
- Real-Time Stamina

### Possible SIP Insights

- Zawodnik rozpoczął zbyt agresywnie.
- Strategia tempa była optymalna.
- Rezerwy energetyczne zostały wykorzystane zbyt wcześnie.

---

# Influence on Sport Intelligence Platform

## Domain Models

- RunningMechanics
- Physiology
- Recovery
- TrainingLoad
- Performance
- RaceStrategy

## Possible APIs

- Running Mechanics API
- Physiology API
- Recovery API
- Training API
- Performance API

## Possible Insights

- Running Economy
- Fatigue Detection
- Injury Risk
- Mechanical Efficiency
- Performance Stability
- Recovery Quality
- Race Strategy Evaluation

## Future Research

- Biomechanika biegu
- Fizjologia wysiłku
- Analiza danych z czujników
- Modele zmęczenia
- Adaptacja treningowa
- Badania nad ekonomią biegu

---

# Influence on SIP

Najważniejsze wnioski dla projektu Sport Intelligence Platform:

1. Dane biomechaniczne są równie ważne jak wynik końcowy.
2. Każda metryka powinna prowadzić do interpretacji, a nie tylko prezentacji liczby.
3. Insight musi być poparty dowodami (Evidence).
4. Trendy są cenniejsze niż pojedyncze pomiary.
5. Kontekst zmienia znaczenie każdej metryki.
6. SIP powinien analizować relacje między metrykami.
7. Analiza biomechaniki wspiera wykrywanie zmęczenia i ryzyka kontuzji.
8. Integracja danych z Garmin, Strava, Polar, COROS, Stryd i innych źródeł zwiększa wartość analizy.
9. Celem SIP jest przekształcenie danych w wiedzę, a wiedzy w decyzje.
10. Performance Intelligence Engine powinien łączyć biomechanikę, fizjologię, historię treningów oraz wynik zawodów w jedną spójną historię sportowca.