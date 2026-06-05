def split_bill(total_bill, people):
    if not isinstance(total_bill, (int, float)) or total_bill <= 0:
        print("Invalid bill amount.")
        return
    if not isinstance(people, int) or people <= 0:
        print("Invalid number of people.")
        return
    share = total_bill // people
    print(f"Each person pays: {share}")

# Using the specified variables
split_bill(1250, 4)