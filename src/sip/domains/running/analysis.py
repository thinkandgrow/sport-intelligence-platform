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