class Product:
    """
    Товар интернет-магазина.
    """
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
    """
    Категория товаров.
    """
    total_categories: int = 0
    total_products: int = 0

    name: str
    description: str
    products: list

    def __init__(self, name: str, description: str, products: list = None) -> None:
        self.name = name
        self.description = description
        if products is None:
            self.products = []
        else:
            self.products = products

        Category.total_categories += 1
        Category.total_products += len(self.products)