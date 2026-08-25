import pytest

from src.models import Category
from src.utils import load_categories_from_json


@pytest.fixture(autouse=True)
def reset_counters():
    Category.total_categories = 0
    Category.total_products = 0


def test_load_categories_from_real_file():
    categories = load_categories_from_json("data/products.json")
    assert len(categories) == 2

    cat1 = categories[0]
    assert cat1.name == "Смартфоны"
    assert cat1.product_count == 3
    # Проверяем, что products – список объектов Product
    assert isinstance(cat1.products, list)
    assert len(cat1.products) == 3
    assert cat1.products[0].name == "Samsung Galaxy C23 Ultra"
    assert cat1.products[1].price == 210000.0

    cat2 = categories[1]
    assert cat2.name == "Телевизоры"
    assert cat2.product_count == 1
    assert cat2.products[0].name == '55" QLED 4K'

    assert Category.total_categories == 2
    assert Category.total_products == 4
