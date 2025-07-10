import pathlib as pl
import pandas as pd


def ingest(path: pl.Path) -> pd.DataFrame:

    if path.suffix != ".csv":
        raise ValueError(f"Expected path of a .csv-file, got {path.suffix}.")

    return pd.read_csv(path)
