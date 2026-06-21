from pathlib import Path

from sip.domains.running.analysis import (
    count_runners_by_country,
    count_runners_by_gender,
    filter_unknown_gender,
)
from sip.domains.running.cleaning import load_results

DATA_FILE = Path("data/raw/warsaw_half_marathon_2026.csv")

df = load_results(DATA_FILE)

print("\n=== FIRST 5 ROWS ===")
print(df.head())

print("\n=== SHAPE ===")
print(df.shape)

print("\n=== DATAFRAME INFO ===")
df.info()

print("\n=== COLUMN NAMES ===")
print(df.columns)

print("\n=== MISSING VALUES ===")
print(df.isna().sum())

print("\n=== DATA TYPES ===")
print(df.dtypes)

print("\n=== RUNNERS BY COUNTRY ===")
print(count_runners_by_country(df))

print("\n=== RUNNERS BY GENDER ===")
print(count_runners_by_gender(df))

print("\n=== UNKNOWN GENDER ===")
print(filter_unknown_gender(df))