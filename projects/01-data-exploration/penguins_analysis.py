"""
Session 4 - Assignment 4: Penguin Data Exploration
Author: Clinton Njoku
Programme: Refonte Learning AI Engineering
Task B: Inspect and Clean
"""

from pathlib import Path
import pandas as pd

# Locate the project folder and raw dataset.
PROJECT_DIR = Path(__file__).resolve().parent
DATA_PATH = PROJECT_DIR / "data" / "penguins.csv"

# Load the dataset without modifying the raw data.
df = pd.read_csv(DATA_PATH)

print("=== 1. DATASET SHAPE ===")
print(df.shape)

print("\n=== 2. FIRST FIVE ROWS ===")
print(df.head())

print("\n=== 3. COLUMN TYPES ===")
df.info()

print("\n=== 4. SUMMARY STATISTICS ===")
print(df.describe().round(2))

print("\n=== 5. MISSING VALUES ===")
print(df.isna().sum())

print("\n=== 6. SPECIES COUNTS ===")
print(df["species"].value_counts())

print("\n=== 7. DUPLICATE ROWS ===")
print(df.duplicated().sum())

print("\n=== 8. RECORDS WITH MISSING MEASUREMENTS ===")

measurement_columns = [
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g"
]

missing_measurements = df[
    df[measurement_columns].isna().any(axis=1)
]

print(missing_measurements.to_string())

print("\n=== 9. RECORDS WITH MISSING SEX ===")

missing_sex = df[df["sex"].isna()]
print(missing_sex.to_string())

print("\n=== 10. MISSING DATA OVERLAP ===")

print("Records missing measurements:", len(missing_measurements))
print("Records missing sex:", len(missing_sex))

print(
    "Records missing both:",
    (df[measurement_columns].isna().any(axis=1) & df["sex"].isna()).sum()
)

print("\n=== 11. DATA CLEANING ===")

# Preserve the original dataset.
clean_df = df.copy()

print("Shape before cleaning:", clean_df.shape)

# Remove records missing any essential physical measurement.
# These records cannot support our measurement-based analysis.
# Retain records with missing sex because their measurements
# remain useful for species and island comparisons.
clean_df = clean_df.dropna(subset=measurement_columns)

print("Shape after removing missing measurements:", clean_df.shape)

# Check duplicate records.
duplicates = clean_df.duplicated().sum()
print("Duplicate rows:", duplicates)

# Remove exact duplicates if any exist.
clean_df = clean_df.drop_duplicates()

print("Shape after duplicate check:", clean_df.shape)

# Confirm column types.
print("\nColumn types after cleaning:")
print(clean_df.dtypes)

# Report remaining missing values.
print("\nRemaining missing values:")
print(clean_df.isna().sum())

# Save cleaned data without changing the original CSV.
OUTPUT_PATH = PROJECT_DIR / "output" / "penguins_cleaned.csv"
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

clean_df.to_csv(OUTPUT_PATH, index=False)

print("\nCleaned dataset saved to:", OUTPUT_PATH)
