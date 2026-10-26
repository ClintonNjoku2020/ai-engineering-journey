
"""
Session 5 - Task B: Deliberately Break Something.

Demonstrate how incorrect date parsing can silently
change monthly record counts.
"""

import pandas as pd


# Dates deliberately written in day/month/year format.
raw_dates = [
    "03/01/2026",
    "04/01/2026",
    "05/01/2026",
    "13/01/2026",
    "02/03/2026",
    "15/03/2026",
]

df = pd.DataFrame({"raw_date": raw_dates})

print("Original dataset:")
print(df)

# Parse dates correctly using the UK day/month/year format.
df["correct_date"] = pd.to_datetime(
    df["raw_date"],
    format="%d/%m/%Y",
    errors="coerce"
)

# Deliberately parse the same dates using the wrong US month/day/year format.
df["incorrect_date"] = pd.to_datetime(
    df["raw_date"],
    format="%m/%d/%Y",
    errors="coerce"
)

print("\n=== CORRECT VS INCORRECT DATE PARSING ===")

print(
    df[["raw_date", "correct_date", "incorrect_date"]].to_string(index=False)
)

print("\nCorrectly parsed dates:", df["correct_date"].notna().sum())
print("Incorrectly parsed dates:", df["incorrect_date"].notna().sum())
print("Invalid dates from incorrect parsing:", df["incorrect_date"].isna().sum())


# Step 4: Compare monthly record counts.

# Group correctly interpreted dates by month.
correct_monthly = (
    df.dropna(subset=["correct_date"])
    .groupby(df["correct_date"].dt.month)
    .size()
)

# Group incorrectly interpreted dates by month.
incorrect_monthly = (
    df.dropna(subset=["incorrect_date"])
    .groupby(df["incorrect_date"].dt.month)
    .size()
)

# Combine results into a side-by-side comparison.
comparison = pd.DataFrame({
    "correct_count": correct_monthly,
    "incorrect_count": incorrect_monthly
}).fillna(0).astype(int)

comparison.index.name = "month"

# Calculate how many records differ by month.
comparison["difference"] = (
    comparison["incorrect_count"] - comparison["correct_count"]
)

print("\n=== MONTHLY COUNT COMPARISON ===")
print(comparison.to_string())

print("\nTotal correct records:", comparison["correct_count"].sum())
print("Total incorrect records:", comparison["incorrect_count"].sum())

# Step 5: Demonstrate the instructor's dayfirst parameter.
# These dates are deliberately ambiguous.
ambiguous_dates = pd.Series([
    "03/01/2026",
    "04/01/2026",
    "05/01/2026",
    "02/03/2026"
])

correct_dayfirst = pd.to_datetime(
    ambiguous_dates,
    format="mixed",
    dayfirst=True,
    errors="coerce"
)

incorrect_dayfirst = pd.to_datetime(
    ambiguous_dates,
    format="mixed",
    dayfirst=False,
    errors="coerce"
)

dayfirst_comparison = pd.DataFrame({
    "raw_date": ambiguous_dates,
    "dayfirst_true": correct_dayfirst,
    "dayfirst_false": incorrect_dayfirst
})

print("\n=== DAYFIRST PARAMETER COMPARISON ===")
print(dayfirst_comparison.to_string(index=False))

# Verify that the two settings produce different dates.
assert (correct_dayfirst != incorrect_dayfirst).all()

print("\nDayfirst experiment passed!")
