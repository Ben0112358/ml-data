import pandas as pd


def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.set_index("Date").pct_change().dropna(axis=0).reset_index()
    return df
