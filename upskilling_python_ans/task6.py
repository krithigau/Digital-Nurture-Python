#KRITHIGA U TASK6
def check_even_odd(number):
    if not isinstance(number, int):
        print("Invalid input. Please provide an integer.")
        return
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")

num = 17
check_even_odd(num)