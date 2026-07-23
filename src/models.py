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
        """Строковое отображение товара: Название, X руб. Остаток: X шт."""
        return f"{self.name}, {self.price:.0f} руб. Остаток: {self.quantity} шт."

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
        """
        Строковое отображение категории:
        Название категории, количество продуктов: X шт.
        где X — сумма всех товаров в категории.
        """
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self) -> str:
        """Список товаров, каждый с новой строки (использует str(product))."""
        if not self.__products:
            return ""
        return "\n".join(str(p) for p in self.__products) + "\n"

    @property
    def product_count(self) -> int:
        """Количество товаров в категории (длина списка)."""
        return len(self.__products)

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.total_products += 1