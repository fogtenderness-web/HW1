from src.utils import load_categories_from_json
from src.models import Order, Smartphone


def main():
    # Пример заказа
    phone = Smartphone(
        "iPhone 15",
        "512GB",
        99999.0,
        5,
        3.2,
        "15",
        512,
        "серый"
    )
    order = Order(phone, 2)
    print(order)
    print()

    categories = load_categories_from_json('data/products.json')
    for category in categories:
        print(category)
        for product in category:
            print(f"  {product}")
        print(f"  Общая стоимость: {category.total_cost:.2f} руб.")
        print()


if __name__ == "__main__":
    main()
