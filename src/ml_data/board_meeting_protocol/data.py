import logging

from ml_data.board_meeting_protocol.clean import clean
from ml_data.board_meeting_protocol.ingest import ingest
from ml_data.board_meeting_protocol.write import write
from ml_data.config import CLEAN_DATA_DIR, ENV_VAR_OUTPUT_SUFFIX
from ml_data.utils import setup_logging


def main() -> None:
    logger = logging.getLogger(__name__)
    logger.info("Recording that this project has no document corpus")
    payload = clean(ingest())
    write(
        payload,
        CLEAN_DATA_DIR / f"data_{ENV_VAR_OUTPUT_SUFFIX}.json",
    )


if __name__ == "__main__":
    setup_logging()
    main()
