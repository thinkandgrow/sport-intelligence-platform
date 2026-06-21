"""
Cleaning utilities for the Running Intelligence domain.

This module is responsible for preparing raw race-result data
for further analysis.
"""

from pathlib import Path

import pandas as pd


def load_results(file_path: str | Path) -> pd.DataFrame:
    """
    Load race results from a CSV file.
    """
    return pd.read_csv(
        file_path,
        sep=";",
        encoding="cp1250",
    )