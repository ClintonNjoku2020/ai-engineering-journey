
"""
Session 5 - Task B: Silent date-parsing errors.

Demonstrate how incorrectly interpreting valid UK dates
changes monthly record counts without producing NaT values.
"""

import pandas as pd


# All dates are ambiguous: day and month are both 12 or below.
# The intended format is UK day/month/year.
raw_dates = [
    "03/01/2026",
    "04/01/2026",
    "05/01/2026",
    "06/01/2026",
    "02/03/2026",
    "04/03/2026",
]

df = pd.DataFrame({"raw_date": raw_dates})

# Correct interpretation: day/month/year (UK).
df["correct_date"] = pd.to_datetime(
    df["raw_date"],
    format="mixed",
    dayfirst=True,
    errors="coerce",
)

# Incorrect interpretation: month/day/year (US).
df["incorrect_date"] = pd.to_datetime(
    df["raw_date"],
    format="mixed",
    dayfirst=False,
    errors="coerce",
)

print("\n=== CORRECT VS INCORRECT DATE PARSING ===")
print(df.to_string(index=False))

# Both interpretations must successfully parse every record.
assert df["correct_date"].notna().all()
assert df["incorrect_date"].notna().all()

# Every date should change meaning when interpreted incorrectly.
assert (df["correct_date"] != df["incorrect_date"]).all()

print("\nMissing dates with correct parsing:",
      df["correct_date"].isna().sum())
print("Missing dates with incorrect parsing:",
      df["incorrect_date"].isna().sum())


# Group both interpretations by calendar month.
correct_monthly = df.groupby(
    df["correct_date"].dt.month
).size()

incorrect_monthly = df.groupby(
    df["incorrect_date"].dt.month
).size()

# Show all 12 months, including those with zero records.
months = range(1, 13)

comparison = pd.DataFrame({
    "correct_count": correct_monthly.reindex(
        months, fill_value=0
    ),
    "incorrect_count": incorrect_monthly.reindex(
        months, fill_value=0
    ),
})

comparison.index.name = "month"

comparison["difference"] = (
    comparison["incorrect_count"] -
    comparison["correct_count"]
)

print("\n=== MONTHLY COUNT COMPARISON ===")
print(comparison.to_string())

print("\nTotal correct records:",
      comparison["correct_count"].sum())
print("Total incorrectly grouped records:",
      comparison["incorrect_count"].sum())

# Both versions contain all six records, but monthly counts differ.
assert comparison["correct_count"].sum() == len(df)
assert comparison["incorrect_count"].sum() == len(df)
assert (comparison["difference"] != 0).any()

# Check specific expected results.
assert comparison.loc[1, "correct_count"] == 4
assert comparison.loc[1, "incorrect_count"] == 0
assert comparison.loc[3, "correct_count"] == 2
assert comparison.loc[3, "incorrect_count"] == 1

print("\nSilent date-parsing experiment passed!")
