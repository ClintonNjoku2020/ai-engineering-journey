
"""Create a penguin species reference table for Session 5 Task C."""

from pathlib import Path
import pandas as pd

data_dir = Path("projects/01-data-exploration/data")

species_reference = pd.DataFrame({
    "species": ["Adelie", "Chinstrap", "Gentoo", "Emperor"],
    "genus": ["Pygoscelis", "Pygoscelis", "Pygoscelis", "Aptenodytes"]
})

output_path = data_dir / "species_reference.csv"
species_reference.to_csv(output_path, index=False)

print("Species reference table:")
print(species_reference.to_string(index=False))
print("\nReference table shape:", species_reference.shape)
print("Saved to:", output_path)
