"""
CSV Data Processor
• Objective: Use file I/O, lists, dictionaries, and comprehensions to analyze CSV data.
• Task: Analyze employee salary data from a CSV file.
"""
import csv
def analyze_salary():
    employees = []
    try:
        with open("employees.csv","r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["salary"] = int(row["salary"])
                employees.append(row)
        salaries = [emp["salary"] for emp in employees]
        average_salary=sum(salaries)/len(salaries)
        print("Employees Records")
        for emp in employees:
            print(emp)
        print("Average Salary:",average_salary)
    except FileNotFoundError:
        print("employees.csv not found")
analyze_salary()
