def read_file_contents(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("File Contents:\n", content)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")

read_file_contents("greeting.txt")