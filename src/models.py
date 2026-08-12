from abc import ABC, abstractmethod
from typing import List, Optional


class BaseProduct(ABC):
    """
    Абстрактный базовый класс для всех продуктов.
    Определяет общие атрибуты и поведение
    """
    name: str
    description: str
    quantity: int

    def __init__(self, name: str, description: str, quantity: int) -> None:
        self.name = name
        self.description = description
        self.quantity = quantity

    @property
    @abstractmethod
    def price(self) -> float:
        """Абстрактное свойство цены. Должно быть переопределено в подклассах."""
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        pass

    def __str__(self) -> str:
        """Строковое представление продукта."""
        return f"{self.name}, {self.price:.0f} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "BaseProduct") -> float:
        """
        Сложение продуктов одного типа.
        Возвращает суммарную стоимость (цена * количество) обоих продуктов.
        """
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных типов")
        return self.price * self.quantity + other.price * other.quantity


class Product(BaseProduct):
    """
    Базовый класс товара. Реализует приватное свойство price с проверками.
    Может использоваться самостоятельно или как родитель для специализированных товаров.
    """
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        super().__init__(name, description, quantity)   # передаём только общие поля
        self.__price = price                            # устанавливаем начальную цену напрямую

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
        """Создаёт Product из словаря. Подходит только для базового класса."""
        return cls(
            name=data["name"],
            description=data["description"],
            price=float(data["price"]),
            quantity=int(data["quantity"])
        )


class Smartphone(Product):
    """Класс для смартфонов."""
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для травы газонной."""
    country: str
    germination_period: int
    color: str

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: int, color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class ProductIterator:
    """Итератор по товарам категории."""
    def __init__(self, category: "Category") -> None:
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
        if not isinstance(product, BaseProduct):
            raise TypeError("В категорию можно добавлять только продукты (BaseProduct или наследники)")
        self.__products.append(product)
        Category.total_products += 1