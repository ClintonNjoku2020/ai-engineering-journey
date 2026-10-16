# Task B: Functions, Properly Written

# Student dataset from Task A

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

# Function 1: Return the highest-scoring student's name
def top_scorer(records):
    """Return the name of the highest scorer, or None if empty."""
    if not records:
        return None
    highest_student = max(
        records,
        key=lambda student: student["score"]
    )
    return highest_student["name"]



# Function 2: Calculate the percentage of passing students

def pass_rate(records, threshold=50):
    """Return the percentage of students meeting the score threshold."""

    if not records:
        return 0.0

    passing_students = [
        student for student in records
        if student["score"] >= threshold
    ]

    number_passed = len(passing_students)
    total_students = len(records)

    rate = (number_passed / total_students) * 100

    return rate




# Function 3: Group student names by country

def group_by_country(records):
    """Return a dictionary mapping countries to lists of student names."""

    groups = {}

    if not records:
        return groups

    for student in records:
        country = student["country"]
        name = student["name"]

        if country not in groups:
            groups[country] = []

        groups[country].append(name)

    return groups



# Function 4: Print a student performance summary

def summarise(records):
    """Print a readable student performance report."""

    if not records:
        print("No student records available.")
        return

    total_students = len(records)

    best_student = top_scorer(records)

    passing_percentage = pass_rate(records)

    country_groups = group_by_country(records)

    print("\n===== STUDENT PERFORMANCE REPORT =====")
    print(f"Total students: {total_students}")
    print(f"Top scorer: {best_student}")
    print(f"Pass rate (threshold 50): {passing_percentage:.1f}%")
    print(f"Countries represented: {len(country_groups)}")

    print("\nStudents grouped by country:")

    for country, names in country_groups.items():
        print(f"{country}: {', '.join(names)}")

    print("======================================")




# 3. Test all four functions
print("Top scorer:", top_scorer(students))
print("Empty list test:", top_scorer([]))

print("Pass rate (threshold 50):", pass_rate(students))
print("Pass rate (threshold 60):", pass_rate(students, threshold=60))
print("Empty list pass rate:", pass_rate([]))

print("Students grouped by country:", group_by_country(students))
print("Empty list grouping:", group_by_country([]))

summarise(students)
summarise([])