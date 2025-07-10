
import pandas as pd
import pathlib as pl

def write(df: pd.DataFrame, path: pl.Path):
    df.to_csv(path)