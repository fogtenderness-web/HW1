class Product:
    """Товар."""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Категория товаров."""
    name: str
    description: str
    products: list  # список объектов Product

    def __init__(self, name: str, description: str, products: list = None) -> None:
        self.name = name
        self.description = description
        if products is None:
            self.products = []
        else:
            self.products = products