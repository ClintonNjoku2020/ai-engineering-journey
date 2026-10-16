# Task A: Comprehensions and Data Structures

# Student records

students = [
    {'name': 'Ada', 'score': 72, 'country': 'UK'},
    {'name': 'Bo', 'score': 45, 'country': 'Nigeria'},
    {'name': 'Chi', 'score': 88, 'country': 'Kenya'},
    {'name': 'Dee', 'score': 51, 'country': 'UK'},
    {'name': 'Maya', 'score': 67, 'country': 'Egypt'},
    {'name': 'Kofi', 'score': 34, 'country': 'Ghana'},
    {'name': 'Lena', 'score': 91, 'country': 'Canada'},
    {'name': 'Sam', 'score': 58, 'country': 'UK'},
]

# Display the number of students
print("Number of students:", len(students))

# Exercise 1: Extract all student names

all_names = [student["name"] for student in students]

print("All student names:", all_names)

# Exercise 2: Extract names of students scoring 60 or above
high_scorers = [
    student["name"] for student in students
    if student["score"] >= 60
]
print("Students scoring 60 or above:", high_scorers)


# Exercise 3: Map student names to their scores

# Map student names to their scores
score_lookup = {
    student["name"]: student["score"]
    for student in students
}
print("Student scores:", score_lookup)


# Exercise 4: Extract unique countries

unique_countries = {
    student["country"] for student in students
}

print("Unique countries:", unique_countries)

print("Number of unique countries:", len(unique_countries))


# Exercise 5: Increase student scores by 10%

adjusted_scores = [
    round(student["score"] * 1.1, 1)
    for student in students
]

print("Scores increased by 10%:", adjusted_scores)

# Exercise 6: Traditional for loop versus list comprehension

# Method 1: Traditional for loop
high_scorers_loop = []

for student in students:
    if student["score"] >= 60:
        high_scorers_loop.append(student["name"])

print("Traditional loop result:", high_scorers_loop)

# Method 2: List comprehension
high_scorers_comprehension = [
    student["name"] for student in students
    if student["score"] >= 60
]
print("List comprehension result:", high_scorers_comprehension)

# Comment on readability:
# I personally find the list comprehension more readable for this task
# because the entire operation (filter + extract) fits in a single,
# self-contained expression. It reads almost like plain English:
# "give me each student's name, for each student, if their score is 60 or above."
# The traditional loop is clearer when the logic grows more complex
# (e.g., multiple conditions, side effects, or nested operations).