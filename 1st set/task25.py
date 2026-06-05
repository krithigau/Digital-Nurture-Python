def add_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return "Invalid inputs Krithi!"
        
    return a + b

print(f"Result of add(5, 3): {add_numbers(5, 3)}")