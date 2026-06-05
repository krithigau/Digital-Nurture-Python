def save_greeting_to_file():
    with open("greeting.txt", "w") as file:
        file.write("Hello World")
    print("Greeting from Krithi successfully saved to greeting.txt")

save_greeting_to_file()