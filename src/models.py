from typing import List, Optional


class Product:
    """Базовый класс для всех товаров."""
    name: str
    description: str
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price  # приватный атрибут
        self.quantity = quantity

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

    def __str__(self) -> str:
        return f"{self.name}, {self.price:.0f} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Сложение товаров разрешено только для экземпляров одного класса."""
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных типов")
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, data: dict) -> "Product":
        """Создаёт товар из словаря. Для базового класса ожидает ключи name, description, price, quantity."""
        return cls(
            name=data["name"],
            description=data["description"],
            price=float(data["price"]),
            quantity=int(data["quantity"])
        )


class Smartphone(Product):
    """Класс для смартфонов."""
    efficiency: float      # производительность (например, частота процессора)
    model: str             # модель
    memory: int            # объём встроенной памяти (ГБ)
    color: str             # цвет

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str) -> None:
        # Вызываем конструктор Product
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для травы газонной."""
    country: str                 # страна-производитель
    germination_period: int      # срок прорастания (дней)
    color: str                   # цвет

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: int, color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color