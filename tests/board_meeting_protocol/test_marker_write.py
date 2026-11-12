import json

from ml_data.board_meeting_protocol.write import write


def test_write_creates_missing_parent_directories(tmp_path):
    path = tmp_path / "data" / "clean" / "data_board.json"
    write({"project": "board_meeting_protocol", "corpus": "none"}, path)
    assert json.loads(path.read_text(encoding="utf-8")) == {
        "project": "board_meeting_protocol",
        "corpus": "none",
    }
