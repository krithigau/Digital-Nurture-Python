"""
Polymorphism
• Objective: Demonstrate polymorphism using method overriding.
• Task: Show different behaviors of the same method (work()) for different employee 
"""
class Employee:
    def work(self):
        print("Employee is working")
class Developer(Employee):
    def work(self):
        print("Developer writes code")
class Tester(Employee):
    def work(Self):
        print("Tester tests applications")
class Analyst(Employee):
    def work(Self):
        print("Analyst analyzes data")
employees=[Developer(),Tester(),Analyst()]
for employee in employees:
    employee.work()
    