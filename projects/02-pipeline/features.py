import logging

import pandas as pd

from config import (
    GROUP_COLUMN,
    MASS_COLUMN,
    LENGTH_COLUMN,
    MASS_CONVERSION_FACTOR,
    MASS_KG_COLUMN,
    MASS_PER_FLIPPER_COLUMN,
    COUNT_COLUMN,
    MEAN_MASS_COLUMN,
    MEAN_RATIO_COLUMN,
    ROUND_DECIMALS,
)

logger = logging.getLogger(__name__)


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add two derived features using configured measurement columns."""
    required = [MASS_COLUMN, LENGTH_COLUMN]

    missing = [
        column for column in required
        if column not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Missing columns required for features: {missing}"
        )

    if df[required].isna().any().any():
        raise ValueError(
            "Missing measurements found. Clean the data first."
        )

    if (df[LENGTH_COLUMN] == 0).any():
        raise ValueError(
            f"{LENGTH_COLUMN} contains zeros; cannot calculate mass ratio."
        )

    result = df.copy()

    result[MASS_KG_COLUMN] = (
        result[MASS_COLUMN] / MASS_CONVERSION_FACTOR
    ).round(ROUND_DECIMALS)

    result[MASS_PER_FLIPPER_COLUMN] = (
        result[MASS_COLUMN] / result[LENGTH_COLUMN]
    ).round(ROUND_DECIMALS)

    logger.info("Added 2 derived features")

    return result


def summarise(
    df: pd.DataFrame,
    group_column: str | None = None,
) -> pd.DataFrame:
    """Calculate counts and mean measurements for each configured group."""
    if group_column is None:
        group_column = GROUP_COLUMN

    required = [
        group_column,
        MASS_KG_COLUMN,
        MASS_PER_FLIPPER_COLUMN,
    ]

    missing = [
        column for column in required
        if column not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Missing columns required for summary: {missing}"
        )

    summary = df.groupby(group_column).agg(
        **{
            COUNT_COLUMN: (group_column, "size"),
            MEAN_MASS_COLUMN: (MASS_KG_COLUMN, "mean"),
            MEAN_RATIO_COLUMN: (MASS_PER_FLIPPER_COLUMN, "mean"),
        }
    ).round(ROUND_DECIMALS)

    logger.info("Created summary for %d groups", len(summary))

    return summary
