import json

from ml_data.board_meeting_protocol.clean import clean
from ml_data.board_meeting_protocol.ingest import ingest
from ml_data.board_meeting_protocol.write import write


def test_marker_roundtrip(tmp_path):
    payload = clean(ingest())
    path = tmp_path / "data_board.json"
    write(payload, path)
    loaded = json.loads(path.read_text(encoding="utf-8"))
    assert loaded["project"] == "board_meeting_protocol"
    assert loaded["corpus"] == "none"
