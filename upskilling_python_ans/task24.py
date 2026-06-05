from math import *

def math_demonstration(number):
    if not isinstance(number, (int, float)) or number < 0:
        print("Invalid positive number Krithi.")
        return
    print(f"Square root of {number}: {sqrt(number):.2f}")
    print(f"{number} squared: {pow(number, 2):.2f}")
    print(f"Value of Pi: {pi:.4f}")

math_demonstration(16)