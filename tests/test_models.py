import pytest
from src.models import Product, Category


@pytest.fixture(autouse=True)
def reset_category_counters():
    Category.total_categories = 0
    Category.total_products = 0


def test_product_initialization():
    product = Product("Молоко", "1 литр, 3.2%", 89.99, 15)
    assert product.name == "Молоко"
    assert product.description == "1 литр, 3.2%"
    assert product.price == 89.99
    assert product.quantity == 15


def test_product_different_values():
    product = Product("Хлеб", "Ржаной", 54.50, 30)
    assert product.name == "Хлеб"
    assert product.price == 54.50
    assert product.quantity == 30


def test_category_initialization_with_products():
    p1 = Product("A", "desc1", 10.0, 5)
    p2 = Product("B", "desc2", 20.0, 10)
    cat = Category("Категория", "Описание", [p1, p2])
    assert cat.name == "Категория"
    assert cat.product_count == 2
    expected_str = "A, 10 руб. Остаток: 5 шт.\nB, 20 руб. Остаток: 10 шт."
    assert cat.products == expected_str


def test_category_initialization_empty_list():
    cat = Category("Пусто", "Нет товаров", [])
    assert cat.product_count == 0
    assert cat.products == ""


def test_category_initialization_none():
    cat = Category("Пусто", "Описание", None)
    assert cat.product_count == 0
    assert cat.products == ""


def test_total_categories_counter():
    assert Category.total_categories == 0
    Category("A", "desc")
    assert Category.total_categories == 1
    Category("B", "desc", [])
    assert Category.total_categories == 2
    Category("C", "desc", [Product("X", "x", 1.0, 1)])
    assert Category.total_categories == 3


def test_total_products_counter():
    assert Category.total_products == 0
    p1 = Product("p1", "d", 1.0, 10)
    p2 = Product("p2", "d", 2.0, 20)
    Category("Cat1", "desc", [p1, p2])
    assert Category.total_products == 2
    Category("Cat2", "desc", [])
    assert Category.total_products == 2
    Category("Cat3", "desc", [p1])
    assert Category.total_products == 3
    Category("Cat4", "desc", None)
    assert Category.total_products == 3


def test_class_attributes_accessible_from_instance():
    cat = Category("Test", "desc", [Product("X", "y", 9.99, 1)])
    assert cat.total_categories == 1
    assert cat.total_products == 1


def test_add_product():
    cat = Category("Тест", "Описание")
    cat.add_product(Product("Товар1", "описание", 100.0, 10))
    assert cat.product_count == 1
    assert cat.products == "Товар1, 100 руб. Остаток: 10 шт."
    cat.add_product(Product("Товар2", "описание2", 200.0, 5))
    assert cat.product_count == 2
    assert cat.products == "Товар1, 100 руб. Остаток: 10 шт.\nТовар2, 200 руб. Остаток: 5 шт."


def test_new_product_from_dict():
    data = {
        "name": "Тестовый товар",
        "description": "Описание",
        "price": 123.45,
        "quantity": 7
    }
    product = Product.new_product(data)
    assert product.name == "Тестовый товар"
    assert product.description == "Описание"
    assert product.price == 123.45
    assert product.quantity == 7


def test_new_product_with_string_numbers():
    data = {
        "name": "Товар",
        "description": "...",
        "price": "99.99",
        "quantity": "5"
    }
    product = Product.new_product(data)
    assert isinstance(product.price, float)
    assert isinstance(product.quantity, int)
    assert product.price == 99.99
    assert product.quantity == 5