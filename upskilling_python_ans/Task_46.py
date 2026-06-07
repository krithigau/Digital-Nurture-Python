"""
API Response Handler
• Objective: Use requests, JSON handling, classes, and error handling to process API
responses.
• Task: Fetch weather data from an API and display temperature and conditions safely
"""
def search_employee():
    employees=[
        {"id":101,"name":"Alice","salay":50000},
        {"id":102,"name":"Bob","salary":60000},
        {"id":103,"name":"Ken","salary":55000}
    ]
    search_id = 102
    for employee in employees:
        if employee["id"] == search_id:
            print("Employee Found")
            print("ID:",employee["id"])
            print("Name:",employee["name"])
            print("Salary:",employee)
            return
        print("Employee Not Found")
search_employee()
