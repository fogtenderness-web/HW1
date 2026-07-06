import pytest
from src.utils import load_categories_from_json
from src.models import Category


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

    expected_lines = [
        "Samsung Galaxy C23 Ultra, 180000 руб. Остаток: 5 шт.\n",
        "Iphone 15, 210000 руб. Остаток: 8 шт.\n",
        "Xiaomi Redmi Note 11, 31000 руб. Остаток: 14 шт.\n"
    ]
    expected_str = "".join(expected_lines)
    assert cat1.products == expected_str

    cat2 = categories[1]
    assert cat2.name == "Телевизоры"
    assert cat2.product_count == 1
    assert cat2.products == '55" QLED 4K, 123000 руб. Остаток: 7 шт.\n'

    assert Category.total_categories == 2
    assert Category.total_products == 4
