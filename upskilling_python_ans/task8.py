def find_salary_extremes(salaries):
    if not isinstance(salaries, list) or len(salaries) == 0:
        print("Please provide a valid list of salaries.")
        return
    for s in salaries:
        if not isinstance(s, (int, float)):
            print("All salaries must be numbers.")
            return
    
    lowest = min(salaries)
    highest = max(salaries)
    
    print(f"Lowest Salary: Rs.{lowest}")
    print(f"Highest Salary: Rs.{highest}")


salary_list = [50000, 75000, 62000, 95000]
find_salary_extremes(salary_list)