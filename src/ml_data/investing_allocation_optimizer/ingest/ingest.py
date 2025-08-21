import pathlib as pl
import pandas as pd
from ml_data.investing_allocation_optimizer.utils import TICKERS
import yfinance as yfin

def ingest(tickers: list) -> pd.DataFrame:
    df = yfin.download(tickers, start="1921-01-01", auto_adjust=True)["Close"]
    df = df.reset_index()
    df.columns.name = None
    return df