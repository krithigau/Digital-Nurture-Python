def calculate_net_salary(salary, tax_rate):
    # INPUT Validate
    if not (isinstance(salary, (int, float)) and isinstance(tax_rate, (int, float))):
        return "Invalid input ! Please provide numbers."
        
    net_salary = salary * (1 - tax_rate)
    print(f"Net Salary: {net_salary:.2f}")

calculate_net_salary(75000.5, 0.18)