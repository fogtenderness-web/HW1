import pytest

from src.models import Category
from src.utils import load_categories_from_json


@pytest.fixture(autouse=True)
def reset_counters():
    """Перед каждым тестом сбрасываем счётчики."""
    Category.total_categories = 0
    Category.total_products = 0


def test_load_categories_from_real_file():
    """
    Тест загрузки категорий и товаров из data/products.json
    """
    # Загружаем данные из реального JSON-файла
    categories = load_categories_from_json("data/products.json")

    # Проверяем количество категорий
    assert len(categories) == 2

    # Проверяем первую категорию (Смартфоны)
    cat1 = categories[0]
    assert cat1.name == "Смартфоны"
    assert len(cat1.products) == 3

    # Проверяем один из товаров первой категории
    product1 = cat1.products[0]
    assert product1.name == "Samsung Galaxy C23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5

    # Проверяем второй товар
    product2 = cat1.products[1]
    assert product2.name == "Iphone 15"
    assert product2.price == 210000.0

    # Проверяем вторую категорию (Телевизоры)
    cat2 = categories[1]
    assert cat2.name == "Телевизоры"
    assert len(cat2.products) == 1
    assert cat2.products[0].name == '55" QLED 4K'
    assert cat2.products[0].price == 123000.0

    # Проверяем обновление глобальных счётчиков
    # При загрузке создано 2 категории и 4 товара (3+1)
    assert Category.total_categories == 2
    assert Category.total_products == 4
