
"""
Session 5 - Task A: Test the reusable cleaning function.
"""

import pandas as pd
from clean import clean_data


# Create a deliberately messy dataset.
raw_data = pd.DataFrame({
    "customer_name": [
        " Ada Lovelace ",
        "BO AMADI",
        "chi okeke",
        "Ada Lovelace",
        "Dee Smith"
    ],
    "country": [
        "UK",
        "uk ",
        "Nigeria",
        "U.K.",
        "kenya "
    ],
    "spend": [
        "1,200.50",
        "890",
        "n/a",
        "1,200.50",
        "2300.00"
    ],
    "age": [36, 28, 41, 36, 199]
})

print("\n=== ORIGINAL DATA ===")
print(raw_data)

# Apply the reusable cleaning function.
cleaned_data = clean_data(raw_data)

print("\n=== CLEANED DATA ===")
print(cleaned_data)

print("\n=== DATA TYPES ===")
print(cleaned_data.dtypes)

print("\n=== MISSING VALUES ===")
print(cleaned_data.isna().sum())

# Verify the cleaning results.
assert cleaned_data.shape == (4, 4)
assert cleaned_data["customer_name"].iloc[0] == "Ada Lovelace"
assert cleaned_data["country"].iloc[0] == "UK"
assert cleaned_data["country"].iloc[1] == "UK"
assert cleaned_data["spend"].iloc[0] == 1200.50
assert pd.isna(cleaned_data["spend"].iloc[2])
assert cleaned_data.duplicated().sum() == 0

# Confirm the original DataFrame was not modified.
assert raw_data.shape == (5, 4)
assert raw_data["customer_name"].iloc[0] == " Ada Lovelace "

print("\nAll cleaning tests passed!")


# Test the cleaning function on a different dataset.
print("\n=== SECOND DATASET TEST ===")

raw_products = pd.DataFrame({
    "product": [" Laptop ", "LAPTOP", "Mouse"],
    "price": ["1,250.00", "1,250.00", "unknown"],
    "quantity": ["5", "5", "10"]
})

cleaned_products = clean_data(
    raw_products,
    title_columns=["product"]
)

print(cleaned_products)

assert cleaned_products.shape == (2, 3)
assert cleaned_products["product"].iloc[0] == "Laptop"
assert cleaned_products["price"].iloc[0] == 1250.0
assert pd.isna(cleaned_products["price"].iloc[1])
assert cleaned_products["quantity"].iloc[1] == 10

print("\nSecond dataset test passed!")
