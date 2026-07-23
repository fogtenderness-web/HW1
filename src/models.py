from typing import List, Optional


class Product:
    name: str
    description: str
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.price:.0f} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        return NotImplemented

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if value < self.__price:
            answer = input("Вы действительно хотите понизить цену? (y/n): ").strip().lower()
            if answer == "y":
                self.__price = value
            else:
                print("Действие отменено")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, data: dict) -> "Product":
        return cls(
            name=data["name"],
            description=data["description"],
            price=float(data["price"]),
            quantity=int(data["quantity"])
        )


class ProductIterator:
    """Итератор для перебора товаров в категории."""
    def __init__(self, category: "Category") -> None:
        # Получаем доступ к приватному списку через name mangling
        self._products = category._Category__products
        self._index = 0

    def __iter__(self) -> "ProductIterator":
        return self

    def __next__(self) -> Product:
        if self._index >= len(self._products):
            raise StopIteration
        product = self._products[self._index]
        self._index += 1
        return product


class Category:
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

    def __str__(self) -> str:
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self) -> ProductIterator:
        """Возвращает итератор для перебора товаров."""
        return ProductIterator(self)

    @property
    def products(self) -> str:
        if not self.__products:
            return ""
        return "\n".join(str(p) for p in self.__products) + "\n"

    @property
    def product_count(self) -> int:
        return len(self.__products)

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.total_products += 1