def next_year_age():
    age_input = input("Enter your current age: ").strip()    
    if not age_input.isdigit():
        print("Invalid input. Please enter a positive whole number.")
        return
        
    age = int(age_input)
    print(f"Next year you'll be {age + 1}")

next_year_age() 