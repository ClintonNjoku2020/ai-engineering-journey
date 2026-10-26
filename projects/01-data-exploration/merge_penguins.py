
"""
Session 5 - Task C: Merge Two Datasets.

Compare inner and left joins between penguin observations
and a species reference table.
"""

from pathlib import Path
import pandas as pd


# Locate the data files.
data_dir = Path("projects/01-data-exploration/data")

# Load both datasets.
penguins = pd.read_csv(data_dir / "penguins.csv")
species_reference = pd.read_csv(
    data_dir / "species_reference.csv"
)

# Print the original shapes.
print("=== DATASET SHAPES BEFORE MERGING ===")
print("Penguins:", penguins.shape)
print("Species reference:", species_reference.shape)

# Inspect the join keys.
print("\nPenguin species:", penguins["species"].unique())
print("Reference species:", species_reference["species"].unique())

# Check the reference table for duplicate species keys.
assert species_reference["species"].is_unique, (
    "The species reference table contains duplicate keys."
)

# INNER JOIN: Keep only penguins with matching species.
inner_merged = penguins.merge(
    species_reference,
    on="species",
    how="inner",
    validate="many_to_one"
)

# LEFT JOIN: Preserve all original penguin observations.
left_merged = penguins.merge(
    species_reference,
    on="species",
    how="left",
    validate="many_to_one",
    indicator=True
)

print("\n=== DATASET SHAPES AFTER MERGING ===")
print("Inner join:", inner_merged.shape)
print("Left join:", left_merged.shape)

# Report the difference in row counts.
row_difference = len(left_merged) - len(inner_merged)
print("Row difference (left - inner):", row_difference)

# Identify observations without reference matches.
print("\n=== LEFT JOIN MATCH RESULTS ===")
print(left_merged["_merge"].value_counts().to_string())

# We choose the left join because the main purpose is to
# preserve every original penguin observation while adding
# scientific genus information from the reference table.
final_merged = left_merged.drop(columns="_merge")

print("\n=== FIRST FIVE MERGED RECORDS ===")
print(final_merged.head().to_string(index=False))

# Verify no original penguin observations were lost.
assert len(final_merged) == len(penguins)

print("\nMerge verification passed!")

# Step 4: Answer a question requiring both datasets.
# Question: What is the average body mass of each penguin
# species, together with its scientific genus?

species_summary = (
    final_merged
    .groupby(["species", "genus"], dropna=False)
    .agg(
        penguin_count=("species", "size"),
        valid_body_mass_count=("body_mass_g", "count"),
        average_body_mass_g=("body_mass_g", "mean")
    )
    .reset_index()
)

species_summary["average_body_mass_g"] = (
    species_summary["average_body_mass_g"].round(2)
)

print("\n=== AVERAGE BODY MASS BY SPECIES AND GENUS ===")
print(species_summary.to_string(index=False))

# Verify that the summary includes all observed species.
assert species_summary["species"].nunique() == 3

# Verify that all observed species have genus information.
assert species_summary["genus"].notna().all()

# Verify that all original penguin observations are counted.
assert species_summary["penguin_count"].sum() == len(penguins)

print("\nSpecies analysis verification passed!")
