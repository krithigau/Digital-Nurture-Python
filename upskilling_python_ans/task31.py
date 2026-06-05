def display_shopping_cart():
    cart = [100, 250, 75]
    if not all(isinstance(item, (int, float)) for item in cart):
        print("Invalid items in cart Krithi. Must be numbers.")
        return
        
    print(f"Shopping Cart Contents: {cart}")

display_shopping_cart()