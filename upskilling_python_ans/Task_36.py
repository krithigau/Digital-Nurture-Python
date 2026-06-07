"""
Set Intersection
• Objective: Find common elements between two sets using a function and basic
validation.
• Task: Identify common skills between two skill sets.
"""
def find_common_skills():
    employee1 = {"Python","SQL","Excel"}
    employee2 = {"Python","Power BI","SQL"}
    if employee1 and employee2:
        common_skills = employee1 & employee2
        print("Common skills:")
        print(common_skills)
    else:
        print("Invalid input")
find_common_skills()