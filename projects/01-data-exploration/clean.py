
"""
Session 5 - Task A: Reusable Data Cleaning Function
AI Engineering Training and Internship Program

Purpose:
Clean a Pandas DataFrame using repeatable data cleaning steps.
"""

import pandas as pd


def clean_data(df, title_columns=None):
    """
    Clean a raw Pandas DataFrame and return a cleaned copy.

    Cleaning steps:
    1. Inspect and report the original DataFrame shape.
    2. Standardise whitespace and capitalisation in text columns.
    3. Replace recognised missing-value placeholders.
    4. Convert suitable text columns to numeric types.
    5. Remove duplicate rows.
    6. Report the final DataFrame shape.

        Parameters:
        df (pd.DataFrame):
            The raw input DataFrame.
        title_columns (list, optional):
            Text columns to standardise using title case.
            Defaults to customer_name, name, and country.
    Returns:
        pd.DataFrame: A cleaned copy of the input DataFrame.
    """
    cleaned_df = df.copy()

    # Select columns whose values should use title case.
    if title_columns is None:
        title_columns = ["customer_name", "name", "country"]
    print("Shape before cleaning:", cleaned_df.shape)

    # Step 1: Clean whitespace and capitalisation in text columns.
    text_columns = cleaned_df.select_dtypes(
        include=["object", "string"]
    ).columns
    for column in text_columns:
        # Strip spaces without changing missing values.
        cleaned_df[column] = cleaned_df[column].map(
            lambda value: value.strip()
            if isinstance(value, str) else value
        )

        # Standardise capitalisation for names and countries.
        if column.lower() in [name.lower() for name in title_columns]:
            cleaned_df[column] = cleaned_df[column].map(
                lambda value: value.title()
                if isinstance(value, str) else value
            )

    # Standardise common UK country variations.
    if "country" in cleaned_df.columns:
        cleaned_df["country"] = cleaned_df["country"].replace(
            {"Uk": "UK", "U.K.": "UK"}
        )

    # Step 2: Replace placeholder strings with proper missing values.
    missing_placeholders = {
        "n/a", "na", "unknown", "none", "null", "-", ""
    }
    for column in cleaned_df.select_dtypes(
        include=["object", "string"]
    ).columns:
        cleaned_df[column] = cleaned_df[column].map(
            lambda value: pd.NA
            if isinstance(value, str)
            and value.strip().lower() in missing_placeholders
            else value
        )

    # Step 3: Convert numeric-looking text columns to numbers.
    # Protect identifiers and categorical codes from conversion.
    excluded_exact = {
        "id", "date", "code", "phone", "postcode", "zip"
    }
    excluded_suffixes = (
        "_id", "_date", "_code", "_phone", "_postcode", "_zip"
    )

    for column in cleaned_df.select_dtypes(
        include=["object", "string"]
    ).columns:
        column_name = str(column).strip().lower()

        if (
            column_name in excluded_exact
            or column_name.endswith(excluded_suffixes)
        ):
            continue


        # Remove commas used as thousands separators.
        numeric_text = cleaned_df[column].map(
            lambda value: value.replace(",", "")
            if isinstance(value, str) else value
        )

        # Convert invalid numeric values to missing values.
        converted = pd.to_numeric(numeric_text, errors="coerce")

        # Convert only when every non-missing original value is numeric.
        non_missing = cleaned_df[column].notna()

        if non_missing.any() and converted[non_missing].notna().all():
            cleaned_df[column] = converted


    # Step 4: Identify and remove fully duplicated rows.
    duplicate_count = cleaned_df.duplicated().sum()

    print("Duplicate rows found:", duplicate_count)

    cleaned_df = cleaned_df.drop_duplicates().reset_index(drop=True)

    print("Duplicate rows removed:", duplicate_count)

    print("Shape after cleaning:", cleaned_df.shape)

    return cleaned_df
