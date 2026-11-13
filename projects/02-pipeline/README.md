# Reusable Data Pipeline

## Project overview

This project implements a modular, reusable Python data pipeline using the Palmer Penguins dataset.

The pipeline loads, validates, cleans and transforms the data, generates summary statistics by species, and saves the results as a CSV file.

## Failure modes

The pipeline was deliberately tested against four failure scenarios to assess the clarity of its error handling.

| Test scenario | Expected behaviour | Observed error message | Result |
|---|---|---|---|
| Required column removed (`species`) | Identify the missing column | `Missing required columns: ['species']` | Passed |
| Empty CSV file | Report that the input file is empty | `Input file is empty: data/empty_test.csv` | Passed |
| Incorrect file path | Identify the missing input file | `Input file not found: data/nonexistent_penguins.csv` | Passed |
| Non-numeric value in `body_mass_g` | Identify the column containing invalid values | `Column 'body_mass_g' contains non-numeric values.` | Passed |

### Failure-mode test observations

All four tests produced clear and understandable error messages.

- Missing columns are detected during data validation.
- Empty files and missing files are handled during data loading.
- Invalid numeric values are rejected during data cleaning.
- Temporary test files were removed after testing, and the original dataset was preserved.

These tests demonstrate that the pipeline handles the tested failure scenarios without silently processing invalid input.

## Configuration and reusability

The pipeline uses `config.py` to manage input and output paths,
required columns, numeric and text columns, grouping columns,
feature names, conversion factors, and rounding precision.

### Second dataset demonstration

The pipeline was tested using a synthetic wildlife dataset
(`data/wildlife.csv`) containing nine records.

The wildlife dataset uses different column names from the
Palmer Penguins dataset:

| Penguins | Wildlife |
|---|---|
| species | animal |
| island | habitat |
| body_mass_g | weight_g |
| flipper_length_mm | body_length_cm |

After updating the configuration and correcting the feature
module to use configuration variables, the wildlife pipeline
ran successfully without further processing-code changes.

Results:

| Animal | Count | Mean mass (kg) | Mean mass/length |
|---|---:|---:|---:|
| Deer | 3 | 67.67 | 422.06 |
| Fox | 3 | 6.57 | 77.16 |
| Rabbit | 3 | 2.00 | 47.17 |

All automated verification assertions passed.

### Assumptions and limitations

- Input datasets must be CSV files with the configured columns.
- Mass measurements must be numeric and expressed in grams.
- Length measurements must be numeric and non-zero.
- Missing numeric measurements are removed during cleaning.
- The mass conversion factor is 1,000 grams per kilogram.
- The mass-to-length ratio uses the original mass values
  divided by the configured length measurements.
- The wildlife dataset is synthetic and used only to
  demonstrate pipeline reusability.
- The meaning and units of the ratio depend on the dataset.

## Automated testing

The project includes five automated tests in `test_pipeline.py`.

The tests verify:

1. `load_data()` loads the expected dataset.
2. `validate_data()` raises a `ValueError` when a required column is missing.
3. `clean_data()` removes rows with missing numeric measurements.
4. `add_features()` generates the correct derived features.
5. `summarise()` produces the expected species counts.

### Running the tests

From the `projects/02-pipeline` directory, run:

```bash
python test_pipeline.py

```

### Test results

All five automated tests passed successfully.

The tests use Python assertions and require no additional
testing framework.

### Reproducibility

To run the complete pipeline:

```bash
python pipeline.py
```

The pipeline uses the settings in `config.py` and saves
the results to `output/species_summary.csv`.
