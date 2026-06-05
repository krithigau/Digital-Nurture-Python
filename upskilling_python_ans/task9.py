def greet_user():
    name = input("Please enter your name: ").strip()
    if not name:
        print("Name cannot be empty. Please try again.")
        return
    print(f"Hello, {name}! Welcome to the Cognizant !")

greet_user() 