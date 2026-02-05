class Product:
    """
    Represents a product in the store.
    Handles product data, stock management, and purchase logic.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """Initializes product. Validates name, price, and quantity."""
        if not name:
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")

        self.name = str(name)
        self.price = float(price)
        self.active = True
        self.set_quantity(quantity)  # Use setter for initial quantity and active state

    def get_quantity(self) -> int:
        """Returns the current stock quantity."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Sets new quantity and updates active state. Raises ValueError if negative."""
        if quantity < 0:
            raise ValueError("Quantity must be >= 0")
        self.quantity = int(quantity)
        if self.get_quantity() == 0:
            self.deactivate()
        else:
            self.activate()

    def is_active(self) -> bool:
        """Returns True if the product is active."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self):
        """Prints a formatted string representing the product."""
        print(f"{self.name}, Price: {self.price:,.2f}, Quantity: {self.get_quantity()}")

    def buy(self, quantity: int) -> float:
        """Processes purchase. Returns total price. Updates stock via setter."""
        if quantity <= 0:
            raise ValueError("Quantity to buy must be positive.")
        if not self.is_active():
            raise ValueError("Product is currently inactive.")
        if quantity > self.get_quantity():
            raise ValueError(f"Insufficient stock. Only {self.get_quantity()} available.")

        new_quantity = self.get_quantity() - int(quantity)
        self.set_quantity(new_quantity)  # Using setter as requested by Shoval

        return float(quantity) * self.price
