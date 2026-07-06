import pytest
from src.utils import load_categories_from_json
from src.models import Category


@pytest.fixture(autouse=True)
def reset_counters():
    """Перед каждым тестом сбрасываем счётчики."""
    Category.total_categories = 0
    Category.total_products = 0


def test_load_categories_from_real_file():
    """Тест загрузки категорий и товаров из data/products.json"""
    categories = load_categories_from_json("data/products.json")

    # Проверяем количество категорий
    assert len(categories) == 2

    # Проверяем первую категорию (Смартфоны)
    cat1 = categories[0]
    assert cat1.name == "Смартфоны"
    assert cat1.product_count == 3

    # Проверяем строковое представление товаров
    expected_lines = [
        "Samsung Galaxy C23 Ultra, 180000 руб. Остаток: 5 шт.",
        "Iphone 15, 210000 руб. Остаток: 8 шт.",
        "Xiaomi Redmi Note 11, 31000 руб. Остаток: 14 шт."
    ]
    expected_str = "\n".join(expected_lines)
    assert cat1.products == expected_str

    # Проверяем вторую категорию (Телевизоры)
    cat2 = categories[1]
    assert cat2.name == "Телевизоры"
    assert cat2.product_count == 1
    assert cat2.products == '55" QLED 4K, 123000 руб. Остаток: 7 шт.'

    # Проверяем обновление глобальных счётчиков
    assert Category.total_categories == 2
    assert Category.total_products == 4