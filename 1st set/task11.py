def convert_kg_to_lbs():
    weight_input = input("Enter weight in kilograms: ").strip()
    try:
        kg = float(weight_input)
        if kg < 0:
            print("Weight cannot be negative.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid decimal number.")
        return
        
    lbs = kg * 2.20462
    print(f"Weight in pounds: {lbs:.2f} lbs")

convert_kg_to_lbs()