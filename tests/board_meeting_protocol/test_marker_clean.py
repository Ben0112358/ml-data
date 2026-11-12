import pytest

from ml_data.board_meeting_protocol.clean import clean


def test_clean_rejects_payload_with_other_corpus():
    payload = {"project": "board_meeting_protocol", "corpus": "documents"}
    with pytest.raises(ValueError):
        clean(payload)


def test_clean_rejects_payload_without_corpus():
    with pytest.raises(ValueError):
        clean({"project": "board_meeting_protocol"})
