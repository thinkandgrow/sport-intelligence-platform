from pathlib import Path

from sip.domains.running.analysis import (
    count_runners,
    count_runners_by_country,
    count_runners_by_gender,
    filter_unknown_gender,
    mean_net_time,
    median_net_time,
    fastest_runner,
    slowest_runner,
    runner,
    runner_net_time,
    runner_name,
    runner_city,
    runner_country,
    runner_team,
    runner_bib_number,
    runner_gun_time,
    runner_average_pace,
    runner_overall_place,
    runner_gender_place,
    runner_category,
    runner_split_5k,
    runner_split_10k,
    runner_split_15k,
    runner_split_20k,
)


from sip.domains.running.mappers import get_runner

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

print("\n=== MEAN NET TIME ===")
print(mean_net_time(df))

print("\n=== MEDIAN NET TIME ===")
print(median_net_time(df))

print("\n=== FASTEST RUNNER ===")
print(fastest_runner(df))

print("\n=== SLOWEST RUNNER ===")
print(slowest_runner(df))

print("\n=== TOTAL RUNNERS ===")
print(count_runners(df))

print("\n=== FIRST RUNNERS ===")
print(df[["Numer", "Imię i nazwisko"]].head(10))

print("\n=== RUNNER TEST ===")
print(runner(df, "M5"))

print("\n=== RUNNER NET TIME ===")
print(runner_net_time(df, "M5"))


print("\n=== RUNNER NAME ===")
print(runner_name(df, "M5"))

print("\n=== RUNNER CITY ===")
print(runner_city(df, "M5"))

print("\n=== RUNNER COUNTRY ===")
print(runner_country(df, "M5"))

print("\n=== RUNNER TEAM ===")
print(runner_team(df, "M5"))

print("\n=== RUNNER BIB NUMBER ===")
print(runner_bib_number(df, "M5"))

print("\n=== RUNNER GUN TIME ===")
print(runner_gun_time(df, "M5"))

print("\n=== RUNNER AVERAGE PACE ===")
print(runner_average_pace(df, "M5"))

print("\n=== RUNNER OVERALL PLACE ===")
print(runner_overall_place(df, "M5"))

print("\n=== RUNNER GENDER PLACE ===")
print(runner_gender_place(df, "M5"))

print("\n=== RUNNER CATEGORY ===")
print(runner_category(df, "M5"))

print("\n=== RUNNER 5K SPLIT ===")
print(runner_split_5k(df, "M5"))

print("\n=== RUNNER 10K SPLIT ===")
print(runner_split_10k(df, "M5"))

print("\n=== RUNNER 15K SPLIT ===")
print(runner_split_15k(df, "M5"))

print("\n=== RUNNER 20K SPLIT ===")
print(runner_split_20k(df, "M5"))

runner_model = get_runner(df, "M5")
print("\n=== RUNNER MODEL ===")
print(runner_model)



