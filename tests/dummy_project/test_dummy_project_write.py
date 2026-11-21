import pandas as pd

from ml_data.dummy_project.write import write


def test_write_creates_missing_parent_directories(tmp_path):
    path = tmp_path / "data" / "clean" / "data_dummy.csv"
    df = pd.DataFrame({"feature_0": [0.5, -1.0], "target": [1, 0]})
    write(df=df, path=path)
    pd.testing.assert_frame_equal(pd.read_csv(path, index_col=0), df)
