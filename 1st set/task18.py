def find_first_even(range_limit):
    if not isinstance(range_limit, int) or range_limit <= 0:
        print("Invalid range limit.")
        return
        
    for i in range(1, range_limit + 1):
        if i % 2 == 0:
            print(f"The first even number is: {i}")
            break

find_first_even(5)