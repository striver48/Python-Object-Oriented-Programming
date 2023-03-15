import csv


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        assert price >= 0, f"Price {price} is less than zero"
        assert quantity >= 0, f"Quantity {quantity} is less than zero"
        # print(f"Init {name}")
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to Execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def create_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            # print(reader)
            # print(items)
        for item in items:
            # print(item)
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}, {self.price}, {self.quantity}')"