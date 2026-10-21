# Palmer Penguins: Exploratory Data Analysis Using Pandas

**Author:** Clinton Njoku  
**Programme:** Refonte Learning — AI Engineering Training and Internship Programme  
**Assignment:** Session 4 — Pandas: Working With Real Data

## 1. Project Overview

This project explores the Palmer Penguins dataset using Python and Pandas. The objective is to practise loading, inspecting, cleaning, filtering and grouping real-world data, then communicate the findings clearly.

The analysis investigates differences in body mass and flipper length across three penguin species and their recorded islands.

## 2. Dataset Description

**Source:** [Palmer Penguins dataset — seaborn-data on GitHub](https://github.com/mwaskom/seaborn-data/blob/master/penguins.csv)

The dataset includes measurements for three penguin species: Adelie, Chinstrap and Gentoo. The recorded variables are species, island, bill length, bill depth, flipper length, body mass and sex.

The original dataset contains **344 records and 7 columns**. Following cleaning, **342 records** remain available for analysis.

## 3. Data Inspection and Cleaning

The dataset was inspected using `shape`, `head()`, `info()`, `describe()`, `isna().sum()`, `value_counts()` and `duplicated().sum()`.

The inspection identified:

- Two records with all four physical measurements missing.
- Eleven records with missing sex information, including the two records with missing measurements.
- Zero exact duplicate rows.
- Appropriate numerical and categorical data types.

**Cleaning decisions:** The two records lacking physical measurements were removed because those measurements were necessary for the analysis. Nine records missing only sex information were retained because their physical measurements remained useful. No imputation or data-type conversion was necessary.

The cleaned dataset contains 342 records and 7 columns, with nine missing sex values remaining. The original CSV was preserved separately.

## 4. Research Questions and Findings

### Question 1: What is the average body mass of each penguin species?

| Species | Average body mass |
|---|---:|
| Adelie | 3,700.66 g |
| Chinstrap | 3,733.09 g |
| Gentoo | 5,076.02 g |

**Finding:** Gentoo penguins have the highest average body mass, approximately 1.38 kg heavier than Adelie penguins. Chinstrap and Adelie have similar average body masses.

### Question 2: How does average flipper length vary across species?

| Species | Average flipper length |
|---|---:|
| Adelie | 189.95 mm |
| Chinstrap | 195.82 mm |
| Gentoo | 217.19 mm |

**Finding:** Gentoo penguins have the longest average flippers, approximately 27.24 mm longer than Adelie penguins. The results suggest that flipper length may help distinguish species, although individual measurements can overlap.

### Question 3: How many penguins weigh more than 5,000 grams, and which species do they belong to?

Of the 342 cleaned records, **61 penguins (17.84%)** weigh more than 5,000 g.

All 61 belong to the Gentoo species. No Adelie or Chinstrap penguins exceed this threshold in the dataset.

**Finding:** Body mass above 5,000 g is associated exclusively with Gentoo penguins in this sample. However, not every Gentoo penguin exceeds that weight.

### Question 4: How many Gentoo penguins have flippers longer than 220 mm?

There are 123 Gentoo penguins in the cleaned dataset.

Of these, **35 (28.46%)** have flippers longer than 220 mm, while 88 have flippers measuring 220 mm or less.

**Finding:** Although Gentoo penguins have the longest average flipper length, fewer than one-third exceed the 220 mm threshold.

### Question 5: How does average body mass vary by species and island?

| Species | Island | Records | Average body mass |
|---|---|---:|---:|
| Adelie | Biscoe | 44 | 3,709.66 g |
| Adelie | Dream | 56 | 3,688.39 g |
| Adelie | Torgersen | 51 | 3,706.37 g |
| Chinstrap | Dream | 68 | 3,733.09 g |
| Gentoo | Biscoe | 123 | 5,076.02 g |

**Finding:** Adelie penguins have similar average body masses across the three islands, with a maximum difference of only 21.27 g. Gentoo penguins on Biscoe Island have the highest group average.

An important limitation is that Gentoo penguins occur only on Biscoe Island and Chinstrap penguins only on Dream Island in this dataset. Consequently, species and island effects cannot be reliably separated through these simple group comparisons.

## 5. Limitations

The analysis is descriptive rather than causal. Observed differences do not establish why penguin measurements vary.

Species and island are associated in the dataset, limiting direct comparisons of island effects. Missing sex information was retained, and no formal statistical significance tests were performed.

## 6. Future Investigations

With additional time, this project could be extended by:

- Creating charts to compare body mass and flipper length distributions.
- Examining relationships between body mass, bill measurements and flipper length.
- Investigating differences between male and female penguins while accounting for missing sex values.
- Evaluating whether physical measurements can predict penguin species using a machine learning classification model.

## 7. Project Files

- `data/penguins.csv` — Original dataset.
- `output/penguins_cleaned.csv` — Cleaned dataset.
- `penguins_analysis.py` — Inspection, cleaning and analytical code.
- `analysis_questions.md` — Five research questions and analytical approach.
- `README.md` — Project documentation and findings.

## 8. Tools and Skills Demonstrated

**Tools:** Python, Pandas, Ubuntu (WSL2), VS Code and Git/GitHub.

**Skills:** CSV data loading, exploratory data analysis, missing-value assessment, duplicate checks, data cleaning, Boolean filtering, grouping, aggregation, reproducible analysis and technical documentation.