class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.quantity = 0

    def display_info(self):
        return f"Product Name: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}"
    def update_quantity(self, amount):
        self.quantity += amount
        return f"Updated Quantity: {self.quantity}"
    def is_in_stock(self):
        return self.quantity > 0
    def total_value(self):
        return self.price * self.quantity
    
item = input("Enter product name: ")
price = int(input("Enter price: "))
product1 = product(item, price)
print(product1.display_info())
new_quantity = int(input("Enter quantity to add: "))
print(product1.update_quantity(new_quantity))
print("Is in stock:", product1.is_in_stock())
product2 = product("Smartphone", 499.99)
print(product2.display_info())
print(product2.update_quantity(0))
print("Is in stock:", product2.is_in_stock())