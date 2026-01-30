class Product:

    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = str(name)
        self.price = float(price)
        self.quantity = int(quantity)
        self.active = True if self.quantity > 0 else False

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity must be >= 0")
        self.quantity = int(quantity)
        self.active = self.quantity > 0

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price:,.2f}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Quantity to buy must be > 0")
        if not self.active:
            raise ValueError("Product is inactive")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available")

        self.quantity -= int(quantity)
        if self.quantity == 0:
            self.deactivate()

        return float(quantity) * self.price
