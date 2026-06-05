def get_nested_salary(company_data, department, employee):
    if not isinstance(company_data, dict):
        return
        
    if department in company_data and employee in company_data[department]:
        salary = company_data[department][employee]
        print(f"{employee} ({department}): ${salary}")
    else:
        print("Employee or Department not found.")

company = {
    "Engineering": {"Shubh": 75000, "Krithiga": 95000},
    "Marketing": {"Alex": 60000}
}
get_nested_salary(company, "Engineering", "Krithiga")