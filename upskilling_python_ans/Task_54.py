"""
Inventory Manager
• Objective: Use classes, inheritance, dictionaries, and sets to manage warehouse
inventory.
• Task: Track products, stock levels, and generate low-stock alerts.
"""
class Product:

    def __init__(self, name, stock):

        self.name = name
        self.stock = stock


class InventoryManager(Product):

    def __init__(self):

        self.inventory = {}

        self.low_stock = set()

    def add_product(self, name, stock):

        self.inventory[name] = stock

    def display_inventory(self):

        print("\nInventory")

        for product, stock in self.inventory.items():

            print(product, "-", stock)

    def check_low_stock(self):

        self.low_stock.clear()

        for product, stock in self.inventory.items():

            if stock < 10:

                self.low_stock.add(product)

    def display_alerts(self):

        print("\nLow Stock Alerts")

        if len(self.low_stock) == 0:

            print("No Low Stock Products")

        else:

            for product in self.low_stock:

                print(product, "- Low Stock")


manager = InventoryManager()

manager.add_product("Laptop", 20)

manager.add_product("Mouse", 5)

manager.add_product("Keyboard", 3)

manager.add_product("Monitor", 15)

manager.display_inventory()

manager.check_low_stock()

manager.display_alerts()