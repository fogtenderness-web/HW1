from src.models import Product, Category
from src.utils import load_categories_from_json


from src.utils import load_categories_from_json
from src.models import Product, Category, Order, Smartphone, LawnGrass

def main():
    # Пример заказа
    phone = Smartphone("iPhone 15", "512GB", 99999.0, 5, 3.2, "15", 512, "серый")
    order = Order(phone, 2)
    print(order)  # Заказ: iPhone 15, 2 шт. × 99999.00 руб. = 199998.00 руб.
    print()

    categories = load_categories_from_json('data/products.json')
    for cat in categories:
        print(cat)   # Категория, количество продуктов: X шт.
        for p in cat:
            print(f"  {p}")   # использует Product.__str__
        print(f"  Общая стоимость: {cat.total_cost:.2f} руб.")
        print()

if __name__ == "__main__":
    main()