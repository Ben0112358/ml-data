import pandas as pd
import pathlib as pl


def write(df: pd.DataFrame, path: pl.Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path)
