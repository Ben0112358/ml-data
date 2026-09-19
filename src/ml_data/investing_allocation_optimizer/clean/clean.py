import logging
import os
from datetime import datetime

import pandas as pd

logger = logging.getLogger(__name__)

BENCHMARK_LABEL = "total-world"


def _parse_asset_history_start() -> datetime | None:
    raw = os.environ.get("ASSET_HISTORY_START", "").strip()
    if not raw:
        return None
    return datetime.strptime(raw, "%Y-%m-%d")


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert prices to simple returns and align rows for joint resampling.

    Default: keep only dates where every asset has a return (common window).
    Optional ASSET_HISTORY_START (YYYY-MM-DD): drop assets whose first
    valid price is after that date instead of truncating the whole panel.
    """
    df = df.copy()
    if "Date" not in df.columns:
        raise ValueError("Expected Date column in raw data")

    cutoff = _parse_asset_history_start()
    price_cols = [c for c in df.columns if c != "Date"]

    if cutoff is not None:
        kept = []
        for col in price_cols:
            first_valid = df.loc[df[col].notna(), "Date"].min()
            if pd.isna(first_valid):
                logger.warning("Dropping %s: no valid prices", col)
                continue
            if pd.Timestamp(first_valid) > pd.Timestamp(cutoff):
                logger.info(
                    "Dropping %s: first valid %s after cutoff %s",
                    col,
                    first_valid,
                    cutoff.date(),
                )
                continue
            kept.append(col)
        price_cols = kept
        df = df[["Date"] + price_cols]

    df = df.set_index("Date")
    rets = df.pct_change()
    n_before = len(rets)

    mask = rets.notna().all(axis=1)
    if not mask.any():
        raise ValueError("No rows with complete returns after pct_change")

    first_ret_dates = {
        col: rets[col].first_valid_index() for col in price_cols
    }
    binding = max(
        price_cols,
        key=lambda c: first_ret_dates[c] or pd.Timestamp.min,
    )
    logger.info(
        "Binding asset (latest first return): %s (%s)",
        binding,
        first_ret_dates[binding],
    )
    for col in price_cols:
        first_ret = rets[col].first_valid_index()
        if first_ret is not None:
            logger.info("First return date for %s: %s", col, first_ret)

    aligned = rets.loc[mask].reset_index()
    n_after = len(aligned)
    logger.info(
        "Aligned return panel: %s rows (dropped %s); "
        "binding constraint is common window across %s assets",
        n_after,
        n_before - n_after,
        len(price_cols),
    )
    if BENCHMARK_LABEL in aligned.columns:
        start = aligned["Date"].min()
        end = aligned["Date"].max()
        logger.info(
            "Effective sample window for %s: %s to %s",
            BENCHMARK_LABEL,
            start,
            end,
        )
    else:
        logger.warning(
            "Benchmark label %s not in cleaned columns: %s",
            BENCHMARK_LABEL,
            list(aligned.columns),
        )

    return aligned
