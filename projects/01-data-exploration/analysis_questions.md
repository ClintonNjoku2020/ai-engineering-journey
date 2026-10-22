# Session 4 - Penguins Data Exploration

## Task C: Seven Analytical Questions

Author: Clinton Njoku

Dataset: Palmer Penguins

### Research Questions

1. What is the average body mass of each penguin species?

2. How does average flipper length vary across penguin species?

3. How many penguins weigh more than 5,000 grams,
   and which species do they belong to?

4. How many Gentoo penguins have flippers longer than 220 mm?

5. How does average body mass vary by species and island?

6. How does average body mass differ between male and
   female penguins within each species?

7. What is the relationship between flipper length and
   body mass, both overall and within each penguin species?

### Analytical Approach

The analysis will use the cleaned Penguins dataset
containing 342 records.

Questions 1, 2 and 5 will use Pandas groupby().

Questions 3 and 4 will use Pandas filtering.

### Additional Analytical Techniques

Question 6 will use multi-column groupby() to compare
average body mass by species and sex.

Question 7 will use Pandas corr() to examine the
relationship between flipper length and body mass,
both overall and separately for each species.

Records with missing sex values will be excluded only
from calculations that require known sex information.

Results will be interpreted in plain English.

### Objective

To investigate how penguin body mass and physical
measurements differ across species and islands.