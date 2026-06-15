import pytest
from src.models import Product, Category


@pytest.fixture(autouse=True)
def reset_category_counters():
    """Сброс счётчиков перед каждым тестом."""
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
    assert len(cat.products) == 2
    assert cat.products[0] is p1
    assert cat.products[1] is p2


def test_category_initialization_empty_list():
    cat = Category("Пусто", "Нет товаров", [])
    assert cat.products == []


def test_category_initialization_none():
    cat = Category("Пусто", "Описание", None)
    assert cat.products == []


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