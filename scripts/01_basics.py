"""Python basics: variables, loops, functions, lists, dictionaries."""

# Variables and f-strings
name = "Student"
print(f"Hello, {name}!")

# Lists and loops
marks = [78, 85, 62, 91, 70]
total = 0
for m in marks:
    total += m
print("Total:", total)
print("Average:", total / len(marks))


# Functions
def grade(score):
    if score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    return "D"


for m in marks:
    print(m, "->", grade(m))

# Dictionaries
student = {"name": "Aarav", "course": "INT108", "marks": 78}
for key, value in student.items():
    print(f"{key}: {value}")
