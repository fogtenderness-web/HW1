from src.utils import load_categories_from_json
from src.models import Category


def main():
    categories = load_categories_from_json('data/products.json')

    print(f"Загружено категорий: {Category.total_categories}")
    print(f"Загружено товаров: {Category.total_products}\n")

    for cat in categories:
        print(f"Категория: {cat.name} ({len(cat.products)} товаров)")
        for product in cat.products:
            print(
                f"  - {product.name}: {product.price:.2f} руб."
                f" (в наличии: {product.quantity} шт.)"
            )
        print()


if __name__ == "__main__":
    main()
