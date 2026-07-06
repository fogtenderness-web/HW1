from typing import List, Optional


class Product:
    """
    Товар интернет-магазина.
    """
    name: str
    description: str
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price  # начальная цена устанавливается без проверки
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для цены."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """
        Сеттер для цены. Если цена <= 0, выводит сообщение и не изменяет значение.
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, data: dict) -> "Product":
        """
        Создаёт объект Product из словаря с ключами:
        name, description, price, quantity.
        """
        return cls(
            name=data["name"],
            description=data["description"],
            price=float(data["price"]),
            quantity=int(data["quantity"])
        )


class Category:
    # (код класса Category без изменений)
    total_categories: int = 0
    total_products: int = 0
    name: str
    description: str

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        self.name = name
        self.description = description
        self.__products: List[Product] = list(products) if products else []

        Category.total_categories += 1
        Category.total_products += len(self.__products)

    @property
    def products(self) -> str:
        if not self.__products:
            return ""
        lines = []
        for product in self.__products:
            lines.append(f"{product.name}, {product.price:.0f} руб. Остаток: {product.quantity} шт.")
        return "\n".join(lines)

    @property
    def product_count(self) -> int:
        return len(self.__products)

    def add_product(self, product: Product) -> None:
        self.__products.append(product)