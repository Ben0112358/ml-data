import logging

import pandas as pd
import yfinance as yfin

logger = logging.getLogger(__name__)


def ingest(ticker_map: dict[str, str]) -> pd.DataFrame:
    """
    Download adjusted close prices and rename columns to asset labels.

    ticker_map maps label -> yfinance symbol (e.g. total-world -> VT).
    """
    symbols = list(ticker_map.values())
    label_by_symbol = {v: k for k, v in ticker_map.items()}

    df = yfin.download(symbols, start="1921-01-01", auto_adjust=True)["Close"]
    if isinstance(df, pd.Series):
        df = df.to_frame()
    df = df.reset_index()
    df.columns.name = None

    rename = {}
    for col in df.columns:
        if col == "Date":
            continue
        if col in label_by_symbol:
            rename[col] = label_by_symbol[col]
        else:
            for sym, label in label_by_symbol.items():
                if str(col) == sym:
                    rename[col] = label
                    break

    df = df.rename(columns=rename)

    for label in ticker_map:
        if label not in df.columns:
            logger.warning("No column for asset label %s after ingest", label)
            continue
        first = df.loc[df[label].notna(), "Date"].min()
        logger.info("Asset %s first valid date: %s", label, first)

    return df
