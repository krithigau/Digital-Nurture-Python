"""
Method Chaining
• Objective: Demonstrate method chaining by returning self from methods.
• Task: Create an employee object, set salary, apply raise, and display final salary.
"""
class Employee:
    def __init__(self,name):
        self.name = name
        self.salary = 0
    def set_salary(self,salary):
        if salary > 0 :
            self.salary = salary
        return self
    def apply_raise(self,amount):
        if amount > 0:
            self.salary+=amount
        return self
    def display(self):
        print("Name:",self.name)
        print("salary:",self.salary)
        return self
emp = Employee("Krithiga")
emp.set_salary(50000).apply_raise(50000).display()