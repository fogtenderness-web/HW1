from typing import List, Optional


class Product:
    """
    Товар интернет-магазина.
    Атрибуты:
        name (str): название
        description (str): описание
        price (float): цена (может быть с копейками)
        quantity (int): количество в наличии (в штуках)
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

    @classmethod
    def new_product(cls, data: dict) -> "Product":
        """
        Создаёт объект Product из словаря.
        Ожидаемые ключи: name, description, price, quantity.
        """
        return cls(
            name=data["name"],
            description=data["description"],
            price=float(data["price"]),
            quantity=int(data["quantity"])
        )


class Category:
    """
    Категория товаров.
    """
    total_categories: int = 0
    total_products: int = 0

    name: str
    description: str

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        self.name = name
        self.description = description
        # Сохраняем копию переданного списка, чтобы внешние изменения не влияли на объект
        self.__products: List[Product] = list(products) if products else []

        # Обновляем общие счётчики
        Category.total_categories += 1
        Category.total_products += len(self.__products)

    @property
    def products(self) -> str:
        """
        Геттер, возвращающий список товаров в виде строки.
        Формат: Название продукта, Цена руб. Остаток: Количество шт.
        Товары разделены переносом строки.
        """
        if not self.__products:
            return ""
        lines = []
        for product in self.__products:
            lines.append(f"{product.name}, {product.price:.0f} руб. Остаток: {product.quantity} шт.")
        return "\n".join(lines)

    @property
    def product_count(self) -> int:
        """Возвращает количество товаров в категории."""
        return len(self.__products)

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию."""
        self.__products.append(product)