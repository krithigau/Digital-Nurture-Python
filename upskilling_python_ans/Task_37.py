"""
 Multiple Instances
• Objective: Create multiple objects from a class and access their attributes.
• Task: Create an employee roster using multiple instances of a class.
"""
class Employee:
    def __init__(self,name):
        self.name = name
    def display(self):
        print("Employee Name:",self.name)
emp1 = Employee("Alice")
emp2 = Employee("Bob")
emp3 = Employee("John")
emp1.display()
emp2.display()
emp3.display()