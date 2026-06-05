def sum_odd_numbers(range_limit):
    if not isinstance(range_limit, int) or range_limit <= 0:
        print("Invalid range limit Krithi")
        return
        
    total_sum = 0
    for i in range(10):
        if i % 2 == 0:
            continue
        total_sum += i
        
    print(f"Sum of odd numbers in range: {total_sum}")
sum_odd_numbers(10)