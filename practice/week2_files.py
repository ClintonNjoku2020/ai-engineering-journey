# Task D: Reading a Real File
# Exercise 1: Open and read the CSV file

with open("data/students.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("CSV file contents:")
print(lines)

# Step 2: Extract the CSV column headings

header = lines[0].strip().split(",")

print("CSV headers:", header)

# Step 3: Convert CSV rows into dictionaries

records = []

for line in lines[1:]:
    values = line.strip().split(",")

    student = dict(zip(header, values))

    records.append(student)

print("First student record:", records[0])
print("Number of records:", len(records))

# Step 4: Convert student scores from strings to integers

for student in records:
    student["score"] = int(student["score"])

print("First student after conversion:", records[0])
print("Score data type:", type(records[0]["score"]))


# Step 5: Calculate the average student score

total_score = sum(student["score"] for student in records)

number_of_students = len(records)

average_score = total_score / number_of_students

print("Total student scores:", total_score)
print("Number of students:", number_of_students)
print(f"Average student score: {average_score:.2f}")