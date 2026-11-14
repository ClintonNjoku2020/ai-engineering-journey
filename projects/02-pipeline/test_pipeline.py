"""Automated tests for the reusable data pipeline."""

import pandas as pd

from config import INPUT_PATH, REQUIRED_COLUMNS
from cleaning import load_data, validate_data, clean_data
from features import add_features, summarise


def test_load_data():
    """Check that the input dataset loads correctly."""
    df = load_data(INPUT_PATH)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 344

    print("PASS: load_data")


def test_validate_data_missing_column():
    """Check that validation rejects a missing required column."""
    df = load_data(INPUT_PATH)
    broken_df = df.drop(columns=["species"])

    try:
        validate_data(broken_df, REQUIRED_COLUMNS)
    except ValueError as error:
        assert "species" in str(error)
    else:
        raise AssertionError(
            "validate_data did not reject a missing column"
        )

    print("PASS: validate_data missing column")


def test_clean_data():
    """Check that cleaning removes missing numeric measurements."""
    df = load_data(INPUT_PATH)
    validated_df = validate_data(df)
    cleaned_df = clean_data(validated_df)

    assert len(cleaned_df) == 342
    assert cleaned_df[
        ["body_mass_g", "flipper_length_mm"]
    ].isna().sum().sum() == 0

    print("PASS: clean_data")


def test_add_features():
    """Check that derived features are calculated correctly."""
    df = clean_data(validate_data(load_data(INPUT_PATH)))
    featured_df = add_features(df)

    assert "mass_kg" in featured_df.columns
    assert "mass_per_flipper" in featured_df.columns

    assert featured_df["mass_kg"].iloc[0] == 3.75
    assert featured_df["mass_per_flipper"].iloc[0] == 20.72

    print("PASS: add_features")


def test_summarise():
    """Check that the species summary is correct."""
    df = clean_data(validate_data(load_data(INPUT_PATH)))
    featured_df = add_features(df)
    summary = summarise(featured_df)

    assert len(summary) == 3
    assert summary.loc["Adelie", "count"] == 151
    assert summary.loc["Chinstrap", "count"] == 68
    assert summary.loc["Gentoo", "count"] == 123

    print("PASS: summarise")


if __name__ == "__main__":
    test_load_data()
    test_validate_data_missing_column()
    test_clean_data()
    test_add_features()
    test_summarise()

    print("\nAll 5 pipeline tests passed successfully.")
