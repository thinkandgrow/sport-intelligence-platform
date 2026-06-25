import pandas as pd


def count_runners_by_country(df: pd.DataFrame) -> pd.Series:
    """
    Count runners by country.
    """
    return df["Kraj"].value_counts()

def count_runners_by_gender(df: pd.DataFrame) -> pd.Series:
    """
    Count runners by gender.
    """
    return df["Płeć"].value_counts()

def filter_unknown_gender(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return runners with unknown gender.
    """
    return df[df["Płeć"] == "U"]

def mean_net_time(df: pd.DataFrame) -> pd.Timedelta:
    """
    Return the mean net finish time.
    """
    return df["Czas netto"].mean()

def median_net_time(df: pd.DataFrame) -> pd.Timedelta:
    """
    Return the median net finish time.
    """
    return df["Czas netto"].median()

def fastest_runner(df: pd.DataFrame) -> pd.Series:
    """
    Return the fastest runner.
    """
    return df.loc[df["Czas netto"].idxmin()]

def slowest_runner(df: pd.DataFrame) -> pd.Series:
    """
    Return the slowest runner.
    """
    return df.loc[df["Czas netto"].idxmax()]

def count_runners(df: pd.DataFrame) -> int:
    """
    Return the total number of runners.
    """
    return len(df)


def runner(df: pd.DataFrame, bib_number: str) -> pd.Series:
    """
    Return the race record for a single runner.
    """
    return df.loc[df["Numer"] == bib_number].iloc[0]

def runner_net_time(df: pd.DataFrame, bib_number: str) -> pd.Timedelta:
    """
    Return the runner's net finish time.
    """
    return runner(df, bib_number)["Czas netto"]

def runner_gun_time(df: pd.DataFrame, bib_number: str) -> str:
    """
    Return the runner's gun finish time.
    """
    return runner(df, bib_number)["Czas brutto"]

def runner_average_pace(df: pd.DataFrame, bib_number: str) -> pd.Timedelta:
    """
    Return the runner's average pace per kilometer.
    """

    net_time = runner_net_time(df, bib_number)

    pace = net_time / 21.0975

    return pace

def runner_name(df: pd.DataFrame, bib_number: str) -> str:
    """
    Return the runner's full name.
    """
    return runner(df, bib_number)["Imię i nazwisko"]

def runner_city(df: pd.DataFrame, bib_number: str) -> str:
    """
    Return the runner's city.
    """
    return runner(df, bib_number)["Miasto"]

def runner_country(df: pd.DataFrame, bib_number: str) -> str:
    """
    Return the runner's country.
    """
    return runner(df, bib_number)["Kraj"]

def runner_team(df: pd.DataFrame, bib_number: str) -> str:
    """
    Return the runner's team.
    """
    return runner(df, bib_number)["Team"]

def runner_bib_number(df: pd.DataFrame, bib_number: str) -> str:
    """
    Return the runner's bib number.
    """
    return runner(df, bib_number)["Numer"]

