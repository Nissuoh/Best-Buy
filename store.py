from products import *


class Store:
    def __init__(self, products: list[Product]):
        self.products: list[Product] = list(products)

    def add_product(self, product):
        pass

    def remove_product(self, product):
        pass

    def get_total_quantity(self) -> int:
        pass

    def get_all_products(self) -> list[Product]:
        pass

    def order(self, shopping_list) -> float:
        pass
