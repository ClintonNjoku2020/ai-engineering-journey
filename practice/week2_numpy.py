# Task C: First Contact With NumPy
# Exercise 1: Create a NumPy array of student scores

import numpy as np

# Scores from Task A
scores = np.array([72, 45, 88, 51, 67, 34, 91, 58])

print("Student scores:", scores)


# Exercise 2: Explore NumPy array properties and statistics

print("Array shape:", scores.shape)
print("Data type:", scores.dtype)

print("Mean score:", scores.mean())
print("Maximum score:", scores.max())
print("Minimum score:", scores.min())

print("Standard deviation:", round(scores.std(), 2))


# Exercise 3: Filter scores above the mean using Boolean indexing
mean_score = scores.mean()
# Create a Boolean mask
above_mean_mask = scores > mean_score
print("Boolean mask:", above_mean_mask)
# Select scores above the mean
above_mean_scores = scores[above_mean_mask]
print("Scores above the mean:", above_mean_scores)

# Exercise 4: Create a 3 by 4 array of random numbers

random_array = np.random.rand(3, 4)

print("Random 3 x 4 array:")
print(random_array)

print("Array shape:", random_array.shape)

print("Total of all elements:", random_array.sum())


# Exercise 5: Add 5 to every student score using vectorisation
adjusted_scores = scores + 5
print("Original scores:", scores)
print("Scores after adding 5:", adjusted_scores)

# Exercise 6: Compare Python list and NumPy execution times

import time

size = 5_000_000

# Create a Python list and NumPy array
py_list = list(range(size))
np_array = np.arange(size)

# Measure Python list comprehension time
start = time.time()

result_list = [x * 2 for x in py_list]

python_time = time.time() - start

print(f"Python list: {python_time:.4f} seconds")


# Measure NumPy vectorisation time
start = time.time()

result_array = np_array * 2

numpy_time = time.time() - start

print(f"NumPy array: {numpy_time:.4f} seconds")

# Exercise 6: Timing comparison results
# Python list comprehension: 0.3689 seconds
# NumPy vectorisation: 0.0350 seconds
# NumPy was approximately 10.54 times faster in this test.
