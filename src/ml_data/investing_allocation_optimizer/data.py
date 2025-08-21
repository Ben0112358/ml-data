import logging
from ml_data.investing_allocation_optimizer.ingest import ingest
from ml_data.investing_allocation_optimizer.clean import clean
from ml_data.investing_allocation_optimizer.write import write
from ml_data.config import RAW_DATA_DIR, CLEAN_DATA_DIR, ENV_VAR_OUTPUT_SUFFIX
from ml_data.utils import setup_logging
from ml_data.investing_allocation_optimizer.utils import TICKERS


def main():
    logger = logging.getLogger(__name__)

    logger.info("Ingesting raw data")
    df_raw = ingest(list(TICKERS.values()))

    logger.info("Writing raw data")
    write(
        df=df_raw,
        path=RAW_DATA_DIR / f"data_{ENV_VAR_OUTPUT_SUFFIX}.csv",
    )

    logger.info("Cleaning raw data")
    df_cleaned = clean(df_raw)

    logger.info("Writing cleaned data")
    write(
        df=df_cleaned,
        path=CLEAN_DATA_DIR / f"data_{ENV_VAR_OUTPUT_SUFFIX}.csv",
    )


if __name__ == "__main__":
    setup_logging()
    main()
