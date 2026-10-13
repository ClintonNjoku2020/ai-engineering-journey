# Task B: Python Practice — Week 1
# Name: Clinton Njoku
# Time taken: 3.5 hrs
# Difficult parts: All the parts are difficult.


# 1. Write a function count_vowels(text) that returns how many vowels are in a string.
def count_vowels(text):
    vowels = "aeiouAEIOU"  # include uppercase too
    count = 0
    for letter in text:
        if letter in vowels:
            count += 1
    return count

# Test the function
result = count_vowels("Hello World")
print(f"The number of vowels is: {result}")

result = count_vowels("PYTHON")
print(f"The number of vowels is: {result}")

result = count_vowels("xyz")
print(f"The number of vowels is: {result}")

# 2. Write a function average(numbers) that returns the mean of a list, and returns 0 if the list is
# empty.
def average(numbers):
    if len(numbers) == 0:      # check if the list is empty
        return 0
    total = sum(numbers)       # add up all the numbers
    return total / len(numbers)  # divide by how many numbers there are

# Test the function
result = average([10, 20, 30, 40])
print(f"The average is: {result}")

result = average([5, 10, 15])
print(f"The average is: {result}")

result = average([])
print(f"The average is: {result}")


# 3. Given scores = {"Ada": 72, "Bo": 45, "Chi": 88, "Dee": 51} , print the names of everyone
# scoring above 50, each on its own line.

scores = {"Ada": 72, "Bo": 45, "Chi": 88, "Dee": 51}

for name, score in scores.items():
    if score > 50:
        print(f"{name}")

# 4. Write a function longest_word(sentence) that returns the longest word in a sentence.
def longest_word(sentence):
    words = sentence.split()   # break the sentence into a list of words
    longest = ""               # start with an empty word
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# Test the function
result = longest_word("I love programming in Python")
print(f"The longest word is: {result}")

result = longest_word("cat dog elephant")
print(f"The longest word is: {result}")

result = longest_word("hi")
print(f"The longest word is: {result}")


# 5. Write a loop that builds a list of the squares of the numbers 1 to 10, then prints the total.
squares = []                    # start with an empty list

for number in range(1, 11):     # 1, 2, 3, ..., 10
    squares.append(number ** 2) # add the square to the list

total = sum(squares)            # add up all the squares
print(f"The squares are: {squares}")
print(f"The total is: {total}")

# 6. Rewrite your estimate_hours function from Assignment 1 so the hours per week is a
# parameter with a default of 13. Call it twice: once with defaults, once with 15 hours per week.

def estimate_hours(weeks, hours_per_week=13):
    total = weeks * hours_per_week
    return total

# Call 1: using the default (13 hours per week)
result = estimate_hours(4)
print(f"4 weeks at 13 hrs/week: {result} hours")

# Call 2: overriding the default (15 hours per week)
result = estimate_hours(4, 15)
print(f"4 weeks at 15 hrs/week: {result} hours")
