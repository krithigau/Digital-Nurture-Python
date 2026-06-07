"""
Gradebook System
• Objective: Use dictionaries, functions, control flow, and file I/O for student grade
management.
• Task: Manage student grades, calculate GPA, save/load data, and compute class
average.
"""
import json


def add_student(grades, name, gpa):

    grades[name] = gpa


def class_average(grades):

    if len(grades) == 0:
        return 0

    return sum(grades.values()) / len(grades)


def save_data(grades):

    with open("grades.json", "w") as file:

        json.dump(grades, file)


def load_data():

    try:

        with open("grades.json", "r") as file:

            return json.load(file)

    except FileNotFoundError:

        return {}


grades = {}

add_student(grades, "Niranjani", 9.1)
add_student(grades, "Rahul", 8.5)
add_student(grades, "Priya", 9.4)

print("Class Average:", class_average(grades))

save_data(grades)

loaded_data = load_data()

print("Loaded Data:")

for name, gpa in loaded_data.items():

    print(name, "-", gpa)