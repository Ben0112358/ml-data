import pandas as pd
import pytest

from ml_data.investing_allocation_optimizer.clean import clean


def test_clean_aligns_common_window():
    df = pd.DataFrame(
        {
            "Date": pd.date_range("2020-01-01", periods=5, freq="D"),
            "total-world": [100.0, 101.0, 102.0, 103.0, 104.0],
            "late": [None, None, 50.0, 51.0, 52.0],
        }
    )
    out = clean(df)
    assert len(out) == 2
    assert out["late"].iloc[-1] == pytest.approx((52.0 / 51.0) - 1.0)


def test_clean_two_assets_full_overlap():
    df = pd.DataFrame(
        {
            "Date": pd.date_range("2020-01-01", periods=4, freq="D"),
            "total-world": [100.0, 101.0, 102.0, 103.0],
            "growth": [200.0, 202.0, 204.0, 206.0],
        }
    )
    out = clean(df)
    assert len(out) == 3
    assert "Date" in out.columns
