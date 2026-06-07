"""
Temperature Converter GUI
• Objective: Use classes, user input, modules, and formatted output.
• Task: Convert temperatures between Celsius, Fahrenheit, and Kelvin.
"""
def add_item(cart, item, price, quantity):

    cart[item] = {
        "price": price,
        "quantity": quantity
    }


def view_cart(cart):

    print("\nShopping Cart")

    for item, details in cart.items():

        print(
            item,
            "Price:", details["price"],
            "Quantity:", details["quantity"]
        )


def calculate_total(cart):

    total = 0

    for details in cart.values():

        total += details["price"] * details["quantity"]

    return total


cart = {}

add_item(cart, "Laptop", 50000, 1)
add_item(cart, "Mouse", 500, 2)
add_item(cart, "Keyboard", 1500, 1)

view_cart(cart)

print("\nTotal Bill:", calculate_total(cart))