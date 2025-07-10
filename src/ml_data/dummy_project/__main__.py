from ml_data.dummy_project.ingest import ingest
from ml_data.dummy_project.clean import clean
from ml_data.dummy_project.write import write
from ml_data.config import RAW_DATA_DIR, CLEAN_DATA_DIR, LOGS_DIR
import logging
from datetime import datetime


def setup_logging():
    log_file_path = LOGS_DIR / f"{datetime.today()}.log"

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(" "message)s"
    )
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        "%(asctime)s -" " %(levelname)s - %(" "message)s"
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    return logger


def main():
    logger = logging.getLogger(__name__)

    logger.info("Ingesting raw data")
    df_raw = ingest(path=RAW_DATA_DIR / "data.csv")

    logger.info("Cleaning raw data")
    df_cleaned = clean(df=df_raw)

    logger.info("Writing cleaned data")
    write(df=df_cleaned, path=CLEAN_DATA_DIR / "data.csv")


if __name__ == "__main__":
    logger = setup_logging()
    main()
