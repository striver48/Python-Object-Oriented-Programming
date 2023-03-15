from item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, broken_phones=0):
        # use super function
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is less than zero"
        self.broken_phones = broken_phones
