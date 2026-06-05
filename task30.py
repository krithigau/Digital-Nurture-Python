def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result: {result:.2f}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Both inputs must be numbers.")

safe_divide(10, 2)
safe_divide('hello', 0)