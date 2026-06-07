"""
Data Analysis Pipeline
• Objective: Use modules, functions, lists, file handling, and error handling together.
• Task: Process sales data from a file and calculate statistics.
"""
import json 
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary=salary
    def __str__(self):
        return f"{self.name} - {self.salary}"
employees = {}
def add_employee(name,salary):
    employee = Employee(name,salary)
    employees[name] = salary
def save_data():
    with open("emps.json","w") as file:
        json.dump(employees,file)
    print("Data saved successfully")
def load_Data():
    try:
        with open("emps.json","r") as file:
            data = json.load(file)
        print("Employee Records")
        for name,salary in data.items():
            print(name,"-",salary)
    except FileNotFoundError:
        print("Employee file not found")
add_employee("Krithiga",50000)
add_employee("Haritha",60000)
save_data()
load_Data()


    
