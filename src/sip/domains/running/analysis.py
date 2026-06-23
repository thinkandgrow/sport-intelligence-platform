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



