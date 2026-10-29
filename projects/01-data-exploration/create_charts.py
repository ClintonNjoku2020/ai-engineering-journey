
"""
Session 5 - Task D: Three Charts

Create three visualisations of the Palmer Penguins dataset
using Matplotlib.

Charts:
1. Bar chart - Average body mass by species
2. Histogram - Flipper length distribution
3. Scatter plot - Flipper length versus body mass
"""

from pathlib import Path

import pandas as pd
import matplotlib

# Save figures to PNG without requiring a display window in WSL.
matplotlib.use("Agg")

import matplotlib.pyplot as plt


# Locate the project files independently of the working directory.
PROJECT_DIR = Path(__file__).resolve().parent
DATA_PATH = PROJECT_DIR / "data" / "penguins.csv"
OUTPUT_DIR = PROJECT_DIR / "output"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load the original Penguins dataset.
penguins = pd.read_csv(DATA_PATH)

print("=== SESSION 5: THREE CHARTS ===")
print("Dataset shape:", penguins.shape)
print("Output folder:", OUTPUT_DIR)
print("Missing values:")
print(penguins.isna().sum())


# ============================================================
# CHART 1: Average body mass by penguin species
# ============================================================

# Calculate the average body mass for each species.
average_mass = (
    penguins.groupby("species")["body_mass_g"]
    .mean()
    .sort_values()
)

print("\n=== CHART 1: AVERAGE BODY MASS ===")
print(average_mass.round(2))

# Create the bar chart.
fig, ax = plt.subplots(figsize=(9, 5))

bars = ax.bar(
    average_mass.index,
    average_mass.values,
    color=["#6FC2D6", "#357CA5", "#14496B"],
    width=0.6
)

# Add a finding-focused title and labelled axes.
ax.set_title(
    "Gentoo penguins have the highest average body mass",
    fontsize=14,
    fontweight="bold",
    pad=15
)

ax.set_xlabel("Penguin species", fontsize=11)
ax.set_ylabel("Average body mass (g)", fontsize=11)

# Start the vertical axis at zero for an accurate comparison.
ax.set_ylim(0, average_mass.max() * 1.18)

# Display the average values above each bar.
for bar in bars:
    height = bar.get_height()
    ax.annotate(
        f"{height:,.0f} g",
        xy=(bar.get_x() + bar.get_width() / 2, height),
        xytext=(0, 5),
        textcoords="offset points",
        ha="center",
        va="bottom",
        fontsize=10
    )

# Use a subtle horizontal grid to improve readability.
ax.grid(axis="y", linestyle="--", alpha=0.25)
ax.set_axisbelow(True)

plt.tight_layout()

# Save the chart for GitHub and the README.
chart_path = OUTPUT_DIR / "average_body_mass_by_species.png"

fig.savefig(chart_path, dpi=200, bbox_inches="tight")
plt.close(fig)

print("\nChart 1 saved to:", chart_path)

# Confirm that the PNG file was created.
assert chart_path.is_file()
assert chart_path.stat().st_size > 0

print("Chart 1 verification passed!")

# ============================================================
# CHART 2: Distribution of penguin flipper lengths
# ============================================================

# Exclude missing flipper measurements.
flipper_lengths = penguins["flipper_length_mm"].dropna()

print("\n=== CHART 2: FLIPPER LENGTH DISTRIBUTION ===")
print("Valid measurements:", len(flipper_lengths))
print("Mean flipper length:", round(flipper_lengths.mean(), 2))
print("Median flipper length:", round(flipper_lengths.median(), 2))

# Create the histogram.
fig, ax = plt.subplots(figsize=(9, 5))

ax.hist(
    flipper_lengths,
    bins=20,
    color="#357CA5",
    edgecolor="white",
    linewidth=1
)

# Add the mean as a reference line.
mean_length = flipper_lengths.mean()

ax.axvline(
    mean_length,
    color="#C45A45",
    linestyle="--",
    linewidth=2,
    label=f"Mean: {mean_length:.1f} mm"
)

# Add a finding-focused title and labelled axes.
ax.set_title(
    "Penguin Flipper Lengths Form Two Broad Clusters",
    fontsize=14,
    fontweight="bold",
    pad=15
)

ax.set_xlabel("Flipper length (mm)", fontsize=11)
ax.set_ylabel("Number of penguins", fontsize=11)

ax.legend(frameon=False)
ax.grid(axis="y", linestyle="--", alpha=0.25)
ax.set_axisbelow(True)

plt.tight_layout()

# Save the histogram as a PNG.
chart_path = OUTPUT_DIR / "flipper_length_distribution.png"

fig.savefig(chart_path, dpi=200, bbox_inches="tight")
plt.close(fig)

print("\nChart 2 saved to:", chart_path)

# Verify that the PNG exists and is not empty.
assert chart_path.is_file()
assert chart_path.stat().st_size > 0

print("Chart 2 verification passed!")

# ============================================================
# CHART 3: Relationship between flipper length and body mass
# ============================================================

# Keep observations with both measurements available.
scatter_data = penguins.dropna(
    subset=["flipper_length_mm", "body_mass_g"]
)

print("\n=== CHART 3: FLIPPER LENGTH VS BODY MASS ===")
print("Valid observations:", len(scatter_data))

# Calculate the Pearson correlation coefficient.
correlation = scatter_data[
    ["flipper_length_mm", "body_mass_g"]
].corr().loc["flipper_length_mm", "body_mass_g"]

print("Pearson correlation:", round(correlation, 3))

# Create the scatter plot.
fig, ax = plt.subplots(figsize=(9, 5))

# Use different colours for the three species.
species_colours = {
    "Adelie": "#357CA5",
    "Chinstrap": "#6FC2D6",
    "Gentoo": "#C45A45"
}

for species, colour in species_colours.items():
    species_data = scatter_data[
        scatter_data["species"] == species
    ]

    ax.scatter(
        species_data["flipper_length_mm"],
        species_data["body_mass_g"],
        label=species,
        color=colour,
        alpha=0.7,
        s=45,
        edgecolors="white",
        linewidths=0.4
    )

# Add a finding-focused title.
ax.set_title(
    "Penguins with longer flippers tend to have greater body mass",
    fontsize=14,
    fontweight="bold",
    pad=15
)

# Label both axes with measurement units.
ax.set_xlabel("Flipper length (mm)", fontsize=11)
ax.set_ylabel("Body mass (g)", fontsize=11)

# Display the species legend.
ax.legend(title="Penguin species", frameon=False)

ax.grid(linestyle="--", alpha=0.2)
ax.set_axisbelow(True)

plt.tight_layout()

# Save the scatter plot.
chart_path = OUTPUT_DIR / "flipper_length_vs_body_mass.png"

fig.savefig(chart_path, dpi=200, bbox_inches="tight")
plt.close(fig)

print("\nChart 3 saved to:", chart_path)

# Verify the saved image exists and is not empty.
assert chart_path.is_file()
assert chart_path.stat().st_size > 0

print("Chart 3 verification passed!")
