
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

# Additional question requiring information from both datasets:
# What percentage of observed penguins belongs to each genus?

genus_summary = (
    final_merged
    .groupby("genus", dropna=False)
    .agg(
        penguin_count=("species", "size"),
        species_count=("species", "nunique")
    )
    .reset_index()
)

genus_summary["percentage"] = (
    genus_summary["penguin_count"] / len(penguins) * 100
).round(2)

print("\n=== PENGUIN OBSERVATIONS BY SCIENTIFIC GENUS ===")
print(genus_summary.to_string(index=False))

# All observed species are assigned to genus Pygoscelis.
assert len(genus_summary) == 1
assert genus_summary.loc[0, "genus"] == "Pygoscelis"
assert genus_summary.loc[0, "penguin_count"] == 344
assert genus_summary.loc[0, "species_count"] == 3
assert genus_summary.loc[0, "percentage"] == 100.0

print("\nGenus-level analysis verification passed!")

# Demonstration only: synthetic observations with an unmatched key.
# These records are not part of the real Palmer Penguins dataset.

print("\n=== SYNTHETIC UNMATCHED-KEY MERGE DEMONSTRATION ===")

demo_observations = pd.DataFrame({
    "observation_id": [1, 2, 3, 4],
    "species": ["Adelie", "Gentoo", "Mystery", "Chinstrap"]
})

demo_reference = pd.DataFrame({
    "species": ["Adelie", "Gentoo", "Chinstrap"],
    "genus": ["Pygoscelis", "Pygoscelis", "Pygoscelis"]
})

demo_inner = demo_observations.merge(
    demo_reference,
    on="species",
    how="inner",
    validate="many_to_one"
)

demo_left = demo_observations.merge(
    demo_reference,
    on="species",
    how="left",
    validate="many_to_one",
    indicator=True
)

print("Synthetic observations:", len(demo_observations))
print("Inner join rows:", len(demo_inner))
print("Left join rows:", len(demo_left))
print("Rows retained only by left join:",
      len(demo_left) - len(demo_inner))

print("\nLeft-join results:")
print(demo_left.to_string(index=False))

# Confirm that an inner join drops the unmatched observation.
assert len(demo_inner) == 3

# Confirm that a left join preserves every original observation.
assert len(demo_left) == 4
unmatched = demo_left.loc[
    demo_left["_merge"] == "left_only"
]
assert len(unmatched) == 1
assert unmatched.iloc[0]["species"] == "Mystery"
assert pd.isna(unmatched.iloc[0]["genus"])
print("\nSynthetic unmatched-key demonstration passed!")
