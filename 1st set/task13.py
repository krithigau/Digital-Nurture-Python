def check_even_odd(number):
    if not isinstance(number, int):
        print("Invalid input. Must be an integer.")
        return
        
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")

num = 8
check_even_odd(num)