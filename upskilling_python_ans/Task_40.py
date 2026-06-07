"""
Class Methods
• Objective: Use a class method as a factory to create objects from a formatted string.
• Task: Create an Employee object from a string like "Shubh,75000".
"""
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    @classmethod
    def from_string(cls,emp_string):
        name,salary=emp_string.split(",")
        salary = int(salary)
        return cls(name,salary)
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
emp = Employee.from_string("Krithiga,75000")
emp.display()