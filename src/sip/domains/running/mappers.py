import pandas as pd

from sip.domains.running.analysis import runner
from sip.domains.running.models import Runner


def get_runner(df: pd.DataFrame, bib_number: str) -> Runner:
    """
    Return a Runner model for the given bib number.
    """

    row = runner(df, bib_number)

    return Runner(
        bib_number=row["Numer"],
        name=row["Imię i nazwisko"],
        city=row["Miasto"],
        country=row["Kraj"],
        team=row["Team"],
    )