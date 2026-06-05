def countdown_timer(start_count):
    if not isinstance(start_count, int) or start_count <= 0:
        print("Invalid count value. Must be a positive integer.")
        return
        
    count = start_count
    while count > 0:
        print(count)
        count -= 1
    print("Krithi..")

countdown_timer(5)