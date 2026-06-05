def get_string_length(text):
    if not isinstance(text, str):
        print("Invalid input Krithi, Please provide a string.")
        return
        
    length = len(text)
    print(f"The length of the string is: {length}")

get_string_length("Hello Krithi")