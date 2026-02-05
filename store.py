from products import Product


class Store:
    """
    Manages a collection of Product objects.
    Provides methods for inventory management and order processing.
    """

    def __init__(self, products: list):
        """Initializes store. Validates that all items are Product instances."""
        self.products = []
        for item in products:
            if not isinstance(item, Product):
                raise ValueError("Store can only be initialized with a list of Product objects.")
            self.products.append(item)

    def add_product(self, product: Product):
        """Adds a Product instance to the store."""
        if isinstance(product, Product):
            self.products.append(product)
        else:
            raise ValueError("Can only add Product instances.")

    def remove_product(self, product: Product):
        """Removes a product from the inventory."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns total items in stock across all products."""
        return sum(p.get_quantity() for p in self.products)

    def get_all_products(self) -> list[Product]:
        """Returns all currently active products."""
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        """Processes an order list and returns the total price."""
        total = 0.0
        for product, quantity in shopping_list:
            try:
                total += product.buy(quantity)
            except ValueError as e:
                raise ValueError(f"Order failed for {product.name}: {e}")
        return total
