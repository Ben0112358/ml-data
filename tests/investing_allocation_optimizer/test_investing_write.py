import pandas as pd

from ml_data.investing_allocation_optimizer.write import write


def test_write_creates_missing_parent_directories(tmp_path):
    path = tmp_path / "data" / "clean" / "data_investing.csv"
    df = pd.DataFrame({"Date": ["2020-01-02"], "total-world": [0.01]})
    write(df=df, path=path)
    pd.testing.assert_frame_equal(pd.read_csv(path), df)
