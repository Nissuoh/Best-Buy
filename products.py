from dataclasses import dataclass


class Product:

    @dataclass
    def __init__(self):
        name: str
        price: float
        quantity: int
        active: True


def get_quantity(self) -> int:
    pass


def set_quantity(self, quantity):
    pass


def is_active(self) -> bool:
    pass


def activate(self):
    pass


def deactivate(self):
    pass


def show(self):
    pass


def buy(self, quantity) -> float:
    pass
