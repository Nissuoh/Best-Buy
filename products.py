class Product:
    def __init__(self, name, price, quantity):
        self.name: str = str(name)
        self.price: float = float(price)
        self.quantity: int = int(quantity)
        self.active: bool = True

        if self.quantity == 0:
            self.active = False

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("quantity must be >= 0")

        self.quantity = int(quantity)

        if self.quantity == 0:
            self.deactivate()
        else:
            self.active = True

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price:.2f}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("quantity to buy must be > 0")
        if not self.active:
            raise ValueError("product is inactive")
        if quantity > self.quantity:
            raise ValueError("not enough stock")

        self.quantity -= int(quantity)

        if self.quantity == 0:
            self.deactivate()

        return float(quantity) * self.price
