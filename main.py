from src.models import Product, Category
from src.utils import load_categories_from_json


def main():
    # Пример создания товара через класс-метод
    data = {
        "name": "Наушники",
        "description": "Беспроводные, с шумоподавлением",
        "price": 7999.00,
        "quantity": 12
    }
    headphones = Product.new_product(data)
    print("Создан товар через new_product:")
    print(f"{headphones.name}, {headphones.price:.0f} руб. Остаток: {headphones.quantity} шт.\n")

    # Загружаем категории из JSON (как раньше)
    categories = load_categories_from_json('data/products.json')
    print(f"Загружено категорий: {Category.total_categories}")
    print(f"Загружено товаров: {Category.total_products}\n")

    for cat in categories:
        print(f"Категория: {cat.name} ({cat.product_count} товаров)")
        if cat.product_count > 0:
            print(cat.products)
        print()


if __name__ == "__main__":
    main()