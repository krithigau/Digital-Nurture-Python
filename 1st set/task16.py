def print_numbers(loop_count):
    if not isinstance(loop_count, int) or loop_count <= 0:
        print("Invalid loop count.")
        return
    for i in range(5):
        print(i + 1)

print_numbers(5)