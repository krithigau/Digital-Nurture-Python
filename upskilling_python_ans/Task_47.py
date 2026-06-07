"""
 Complete Calculator Program
• Objective: Combine input, functions, error handling.
• Task: Build a robust calculator that supports + , - , * , /.
"""
def calculate(a, b, op):

    if op == "+":
        return a + b

    elif op == "-":
        return a - b

    elif op == "*":
        return a * b

    elif op == "/":
        return a / b

    else:
        return "Invalid Operator"


try:

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    operation = input("Enter Operation (+,-,*,/): ")

    result = calculate(num1, num2, operation)

    print("Result:", result)

except ZeroDivisionError:

    print("Cannot divide by zero")

except ValueError:

    print("Please enter valid numbers")