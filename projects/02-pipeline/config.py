
from pathlib import Path

# Project directories
PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"
OUTPUT_DIR = PROJECT_DIR / "output"

# Input and output files
INPUT_PATH = DATA_DIR / "penguins.csv"
OUTPUT_PATH = OUTPUT_DIR / "species_summary.csv"

# Required dataset columns
REQUIRED_COLUMNS = [
    "species",
    "island",
    "body_mass_g",
    "flipper_length_mm",
]

# Columns used during cleaning
NUMERIC_COLUMNS = [
    "body_mass_g",
    "flipper_length_mm",
]

TEXT_COLUMNS = [
    "species",
    "island",
]

# Analysis configuration
GROUP_COLUMN = "species"

# Measurement columns used for feature calculations
MASS_COLUMN = "body_mass_g"
LENGTH_COLUMN = "flipper_length_mm"

# Feature conversion
MASS_CONVERSION_FACTOR = 1000

# Derived feature names
MASS_KG_COLUMN = "mass_kg"
MASS_PER_FLIPPER_COLUMN = "mass_per_flipper"

# Summary output column names
COUNT_COLUMN = "count"
MEAN_MASS_COLUMN = "mean_mass_kg"
MEAN_RATIO_COLUMN = "mean_ratio"

# Numeric precision for calculated features
ROUND_DECIMALS = 2
