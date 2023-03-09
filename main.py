class Item:
    def __init__(self, name: str, price: float, quantity: int):
        assert price >= 0, f"Price {price} is less than zero"
        assert quantity >= 0, f"Quantity {quantity} is less than zero"
        print(f"Init {name}")
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("phone", 100, 5)
item2 = Item("laptop", 1000, 3)
item2.has_numpad = False

print(item1.calculate_total_price())
print(item2.calculate_total_price())