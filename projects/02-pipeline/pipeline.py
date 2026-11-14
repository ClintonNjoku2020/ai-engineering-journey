import logging

from config import INPUT_PATH, OUTPUT_PATH
from cleaning import load_data, validate_data, clean_data
from features import add_features, summarise


def run_pipeline():
    """Run the complete data processing pipeline."""

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    logger = logging.getLogger(__name__)

    logger.info("Starting data pipeline")

    # Step 1: Load data
    df = load_data(INPUT_PATH)

    # Step 2: Validate data
    df = validate_data(df)

    # Step 3: Clean data
    cleaned_df = clean_data(df)

    # Step 4: Generate derived features
    featured_df = add_features(cleaned_df)

    # Step 5: Generate summary statistics
    summary = summarise(featured_df)

    # Step 6: Save output
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(OUTPUT_PATH)

    logger.info("Pipeline completed successfully")
    logger.info("Output saved to %s", OUTPUT_PATH)

    return summary


if __name__ == "__main__":
    run_pipeline()
