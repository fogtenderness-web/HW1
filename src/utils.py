import json
from typing import List
from src.models import Product, Category


def load_categories_from_json(file_path: str) -> List[Category]:
    """
    Читает JSON-файл с категориями и товарами.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    categories = []
    for cat_dict in data:
        product_objects = []
        for prod_dict in cat_dict.get('products', []):
            product = Product(
                name=prod_dict['name'],
                description=prod_dict['description'],
                price=float(prod_dict['price']),
                quantity=int(prod_dict['quantity'])
            )
            product_objects.append(product)
        category = Category(
            name=cat_dict['name'],
            description=cat_dict['description'],
            products=product_objects
        )
        categories.append(category)
    return categories