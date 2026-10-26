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


def test_clean_requires_date_column():
    df = pd.DataFrame({"total-world": [100.0, 101.0, 102.0]})
    with pytest.raises(ValueError):
        clean(df)


def test_clean_raises_when_no_complete_returns():
    df = pd.DataFrame(
        {
            "Date": pd.date_range("2020-01-01", periods=3, freq="D"),
            "total-world": [100.0, 101.0, 102.0],
            "empty": [None, None, None],
        }
    )
    with pytest.raises(ValueError):
        clean(df)


def test_clean_history_start_drops_late_asset(monkeypatch):
    monkeypatch.setenv("ASSET_HISTORY_START", "2020-01-02")
    df = pd.DataFrame(
        {
            "Date": pd.date_range("2020-01-01", periods=5, freq="D"),
            "total-world": [100.0, 101.0, 102.0, 103.0, 104.0],
            "late": [None, None, 50.0, 51.0, 52.0],
        }
    )
    out = clean(df)
    assert "late" not in out.columns
    assert len(out) == 4


def test_clean_history_start_drops_asset_without_prices(monkeypatch):
    monkeypatch.setenv("ASSET_HISTORY_START", "2020-01-02")
    df = pd.DataFrame(
        {
            "Date": pd.date_range("2020-01-01", periods=4, freq="D"),
            "total-world": [100.0, 101.0, 102.0, 103.0],
            "empty": [None, None, None, None],
        }
    )
    out = clean(df)
    assert "empty" not in out.columns
    assert len(out) == 3
