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

# ==================================================
# TASK C: FIVE ANALYTICAL QUESTIONS
# ==================================================

print("\n=== QUESTION 1 ===")
print("What is the average body mass of each penguin species?")

# Group the cleaned data by species.
# Calculate the average body mass for each group.
average_mass = (
    clean_df.groupby("species")["body_mass_g"]
    .mean()
    .round(2)
)

print("\nAverage body mass by species (grams):")
print(average_mass)

# ==================================================
# QUESTION 2: AVERAGE FLIPPER LENGTH BY SPECIES
# ==================================================

print("\n=== QUESTION 2 ===")
print("How does average flipper length vary across penguin species?")

# Group the cleaned dataset by species.
# Calculate the average flipper length in millimetres.
average_flipper = (
    clean_df.groupby("species")["flipper_length_mm"]
    .mean()
    .round(2)
)

print("\nAverage flipper length by species (mm):")
print(average_flipper)

# ==================================================
# QUESTION 3: PENGUINS WEIGHING MORE THAN 5000 GRAMS
# ==================================================

print("\n=== QUESTION 3 ===")
print("How many penguins weigh more than 5,000 grams,")
print("and which species do they belong to?")

# Filter penguins weighing strictly more than 5000 grams.
heavy_penguins = clean_df[clean_df["body_mass_g"] > 5000]

# Count the filtered records.
heavy_count = len(heavy_penguins)

print("\nTotal penguins weighing more than 5000 g:")
print(heavy_count)

# Count the heavy penguins by species.
heavy_species_counts = heavy_penguins["species"].value_counts()

print("\nHeavy penguins by species:")
print(heavy_species_counts)

# ==================================================
# QUESTION 4: GENTOO PENGUINS WITH LONG FLIPPERS
# ==================================================

print("\n=== QUESTION 4 ===")
print("How many Gentoo penguins have flippers longer than 220 mm?")

# Filter using two conditions:
# 1. Species must be Gentoo.
# 2. Flipper length must be greater than 220 mm.
long_flipper_gentoo = clean_df[
    (clean_df["species"] == "Gentoo")
    & (clean_df["flipper_length_mm"] > 220)
]

# Count the penguins that satisfy both conditions.
long_flipper_count = len(long_flipper_gentoo)

print("\nNumber of Gentoo penguins with flippers over 220 mm:")
print(long_flipper_count)

# Calculate the total number of Gentoo penguins.
total_gentoo = (clean_df["species"] == "Gentoo").sum()

# Calculate the percentage of Gentoo penguins
# whose flippers exceed 220 mm.
percentage = (long_flipper_count / total_gentoo) * 100

print("\nTotal Gentoo penguins:", total_gentoo)
print(f"Percentage with flippers over 220 mm: {percentage:.2f}%")

# ==================================================
# QUESTION 5: AVERAGE BODY MASS BY SPECIES AND ISLAND
# ==================================================

print("\n=== QUESTION 5 ===")
print("How does average body mass vary by species and island?")

# Group penguins by both species and island.
# Calculate the mean body mass for each group.
average_mass_by_island = (
    clean_df.groupby(["species", "island"])["body_mass_g"]
    .mean()
    .round(2)
)

print("\nAverage body mass by species and island (grams):")
print(average_mass_by_island)

# Count observations in each species-island group.
group_counts = (
    clean_df.groupby(["species", "island"])
    .size()
)

print("\nNumber of penguins in each group:")
print(group_counts)

# ==================================================
# QUESTION 6: BODY MASS BY SPECIES AND SEX
# ==================================================

print("\n=== QUESTION 6 ===")
print("How does average body mass differ between male and "
      "female penguins within each species?")

# Exclude missing sex values only for this analysis.
sex_df = clean_df.dropna(subset=["sex"]).copy()

# Group by species and sex, then calculate
# the number of penguins and average body mass.
sex_mass_summary = (
    sex_df.groupby(["species", "sex"])
    .agg(
        count=("body_mass_g", "size"),
        average_mass_g=("body_mass_g", "mean")
    )
    .round(2)
)

print("\nAverage body mass by species and sex:")
print(sex_mass_summary)

# Compare male and female averages within each species.
sex_mass_comparison = (
    sex_df.groupby(["species", "sex"])["body_mass_g"]
    .mean()
    .unstack()
)

sex_mass_comparison["male_minus_female_g"] = (
    sex_mass_comparison["MALE"]
    - sex_mass_comparison["FEMALE"]
)

print("\nMale minus female average body mass (grams):")
print(sex_mass_comparison["male_minus_female_g"].round(2))

print("\nRecords included:", len(sex_df))
print("Records excluded due to missing sex:",
      clean_df["sex"].isna().sum())


# ==================================================
# QUESTION 7: FLIPPER LENGTH AND BODY MASS CORRELATION
# ==================================================

print("\n=== QUESTION 7 ===")
print(
    "What is the relationship between flipper length and "
    "body mass, overall and within each species?"
)

# Calculate the overall Pearson correlation.
overall_correlation = clean_df[
    ["flipper_length_mm", "body_mass_g"]
].corr().loc["flipper_length_mm", "body_mass_g"]

print("\nOverall Pearson correlation:")
print(round(overall_correlation, 3))

# Calculate the correlation separately for each species.
print("\nPearson correlation by species:")

for species, species_data in clean_df.groupby("species"):
    correlation = species_data[
        ["flipper_length_mm", "body_mass_g"]
    ].corr().loc["flipper_length_mm", "body_mass_g"]

    print(
        f"{species}: r = {correlation:.3f} "
        f"(n = {len(species_data)})"
    )
