import logging
from ml_data.dummy_project.ingest import ingest
from ml_data.dummy_project.clean import clean
from ml_data.dummy_project.write import write
from ml_data.config import RAW_DATA_DIR, CLEAN_DATA_DIR
from ml_data.utils import setup_logging


def main():
    logger = logging.getLogger(__name__)
    logger.info("Ingesting raw data")
    df_raw = ingest(path=RAW_DATA_DIR / "data.csv")

    logger.info("Cleaning raw data")
    df_cleaned = clean(df=df_raw)

    logger.info("Writing cleaned data")
    write(df=df_cleaned, path=CLEAN_DATA_DIR / "data.csv")


if __name__ == "__main__":
    setup_logging()
    main()
