import logging
from pathlib import Path

import pandas as pd

from config import NUMERIC_COLUMNS, TEXT_COLUMNS

logger = logging.getLogger(__name__)


def load_data(path: str | Path) -> pd.DataFrame:
    """Load a non-empty CSV file into a Pandas DataFrame.

    Args:
        path: Location of the input CSV file.

    Returns:
        The loaded DataFrame.

    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If the file is empty or contains no data rows.
    """
    logger.info("Loading data from %s", path)

    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {path}") from None
    except pd.errors.EmptyDataError:
        raise ValueError(f"Input file is empty: {path}") from None

    if df.empty:
        raise ValueError(f"Input file contains no data rows: {path}")

    logger.info(
        "Loaded %d rows and %d columns",
        df.shape[0],
        df.shape[1],
    )

    return df


def validate_data(
    df: pd.DataFrame,
    required_columns: list[str] | None = None,
) -> pd.DataFrame:
    """Check that the DataFrame contains all required columns.

    Args:
        df: DataFrame to validate.
        required_columns: Column names that must be present.

    Returns:
        The validated DataFrame.

    Raises:
        ValueError: If one or more required columns are missing.
    """
    if required_columns is None:
        from config import REQUIRED_COLUMNS
        required_columns = REQUIRED_COLUMNS

    missing = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    logger.info(
        "Validation passed: all %d required columns are present",
        len(required_columns),
    )

    return df


def clean_data(
    df: pd.DataFrame,
    numeric_columns: list[str] = NUMERIC_COLUMNS,
    text_columns: list[str] = TEXT_COLUMNS,
) -> pd.DataFrame:
    """Convert numeric columns, remove missing measurements and standardise text.

    Args:
        df: DataFrame to clean.
        numeric_columns: Columns that must contain numeric values.
        text_columns: Text columns to standardise.

    Returns:
        A cleaned copy of the DataFrame.

    Raises:
        ValueError: If a numeric column contains non-numeric values.
    """
    df = df.copy()

    before = len(df)

    # Convert numeric columns and report invalid values clearly.
    for column in numeric_columns:
        try:
            df[column] = pd.to_numeric(df[column], errors="raise")
        except (ValueError, TypeError) as error:
            raise ValueError(
                f"Column '{column}' contains non-numeric values."
            ) from error

    # Remove rows with missing numeric measurements.
    df = df.dropna(subset=numeric_columns).copy()

    # Standardise text columns.
    for column in text_columns:
        df[column] = (
            df[column]
            .astype("string")
            .str.strip()
            .str.title()
        )

    after = len(df)

    logger.info(
        "Cleaning removed %d rows (%d -> %d)",
        before - after,
        before,
        after,
    )

    return df
