import builtins

import pytest

from src.models import Category, LawnGrass, Product, Smartphone


@pytest.fixture(autouse=True)
def reset_category_counters():
    Category.total_categories = 0
    Category.total_products = 0


# ---------- Тесты Product ----------
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


def test_new_product_from_dict():
    data = {
        "name": "Тестовый товар",
        "description": "Описание",
        "price": 123.45,
        "quantity": 7,
    }
    product = Product.new_product(data)
    assert product.name == "Тестовый товар"
    assert product.description == "Описание"
    assert product.price == 123.45
    assert product.quantity == 7


def test_new_product_with_string_numbers():
    data = {"name": "Товар", "description": "...", "price": "99.99", "quantity": "5"}
    product = Product.new_product(data)
    assert isinstance(product.price, float)
    assert isinstance(product.quantity, int)
    assert product.price == 99.99
    assert product.quantity == 5


def test_product_str():
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    expected = "Телефон, 50000 руб. Остаток: 10 шт."
    assert str(product) == expected


def test_product_addition():
    p1 = Product("Товар A", "описание", 100.0, 10)  # стоимость 1000
    p2 = Product("Товар B", "описание", 200.0, 2)  # стоимость 400
    result = p1 + p2
    assert result == 1400.0
    assert isinstance(result, float)


def test_product_addition_different_prices():
    p1 = Product("A", "", 50.5, 3)  # 151.5
    p2 = Product("B", "", 99.99, 1)  # 99.99
    result = p1 + p2
    assert result == 251.49


def test_product_addition_invalid_type():
    p1 = Product("A", "", 10.0, 5)
    with pytest.raises(TypeError):
        _ = p1 + "не продукт"


def test_addition_different_subclasses_raises():
    phone = Smartphone("A", "", 100, 1, 1.0, "M", 64, "black")
    grass = LawnGrass("B", "", 10, 1, "RU", 7, "green")
    with pytest.raises(TypeError):
        _ = phone + grass


# ---------- Тесты Category ----------
def test_category_initialization_with_products():
    p1 = Product("A", "desc1", 10.0, 5)
    p2 = Product("B", "desc2", 20.0, 10)
    cat = Category("Категория", "Описание", [p1, p2])
    assert cat.name == "Категория"
    assert cat.product_count == 2
    # products теперь список
    assert cat.products == [p1, p2]
    assert cat.total_quantity == 15
    assert cat.total_cost == 250.0  # 10*5 + 20*10 = 50+200=250


def test_category_initialization_empty_list():
    cat = Category("Пусто", "Нет товаров", [])
    assert cat.product_count == 0
    assert cat.products == []
    assert cat.total_quantity == 0
    assert cat.total_cost == 0.0


def test_category_initialization_none():
    cat = Category("Пусто", "Описание", None)
    assert cat.product_count == 0
    assert cat.products == []


def test_add_product():
    cat = Category("Тест", "Описание")
    p1 = Product("Товар1", "описание", 100.0, 10)
    cat.add_product(p1)
    assert cat.product_count == 1
    assert cat.products == [p1]
    assert cat.total_quantity == 10
    assert cat.total_cost == 1000.0

    p2 = Product("Товар2", "описание2", 200.0, 5)
    cat.add_product(p2)
    assert cat.product_count == 2
    assert cat.products == [p1, p2]
    assert cat.total_quantity == 15
    assert cat.total_cost == 2000.0


def test_category_iteration():
    p1 = Product("A", "desc1", 10.0, 5)
    p2 = Product("B", "desc2", 20.0, 10)
    p3 = Product("C", "desc3", 30.0, 15)
    cat = Category("Категория", "Описание", [p1, p2, p3])

    products_list = list(cat)
    assert len(products_list) == 3
    assert products_list[0] is p1
    assert products_list[1] is p2
    assert products_list[2] is p3


def test_category_iteration_stop():
    cat = Category("Пустая", "Нет товаров")
    with pytest.raises(StopIteration):
        iterator = iter(cat)
        next(iterator)


# ---------- Тесты цены ----------
def test_product_price_getter():
    product = Product("Тест", "описание", 100.0, 10)
    assert product.price == 100.0


def test_product_price_setter_increase_no_input(monkeypatch):
    product = Product("Товар", "описание", 100.0, 5)
    monkeypatch.setattr(
        builtins, "input", lambda _: pytest.fail("input не должен вызываться")
    )
    product.price = 150.0
    assert product.price == 150.0


def test_product_price_setter_decrease_confirmation_yes(monkeypatch):
    product = Product("Товар", "описание", 200.0, 5)
    monkeypatch.setattr(builtins, "input", lambda _: "y")
    product.price = 150.0
    assert product.price == 150.0


def test_product_price_setter_decrease_confirmation_no(monkeypatch, capsys):
    product = Product("Товар", "описание", 200.0, 5)
    monkeypatch.setattr(builtins, "input", lambda _: "n")
    product.price = 150.0
    captured = capsys.readouterr()
    assert "Действие отменено" in captured.out
    assert product.price == 200.0


def test_product_price_setter_zero(monkeypatch, capsys):
    product = Product("Товар", "описание", 100.0, 5)
    monkeypatch.setattr(
        builtins, "input", lambda _: pytest.fail("input не должен вызываться")
    )
    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 100.0


def test_product_price_setter_negative(monkeypatch, capsys):
    product = Product("Товар", "описание", 100.0, 5)
    monkeypatch.setattr(
        builtins, "input", lambda _: pytest.fail("input не должен вызываться")
    )
    product.price = -10.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 100.0


def test_product_init_mixin_output_product(capsys):
    _ = Product("Товар", "Описание", 50.0, 10)
    captured = capsys.readouterr()
    assert "Product(name='Товар', description='Описание', quantity=10)" in captured.out


def test_product_init_mixin_output_smartphone(capsys):
    _ = Smartphone("Samsung", "Модель", 30000.0, 5, 2.5, "S23", 128, "черный")
    captured = capsys.readouterr()
    assert "Smartphone(name='Samsung', description='Модель', quantity=5)" in captured.out


def test_product_zero_quantity_raises_value_error():
    with pytest.raises(ValueError) as exc_info:
        Product("Товар", "Описание", 100.0, 0)
    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"


def test_smartphone_zero_quantity_raises():
    with pytest.raises(ValueError):
        Smartphone("Phone", "desc", 100.0, 0, 2.0, "Model", 64, "black")


def test_category_average_price():
    p1 = Product("A", "", 100.0, 5)
    p2 = Product("B", "", 200.0, 3)
    cat = Category("Тест", "Описание", [p1, p2])
    assert cat.average_price() == 150.0   # (100 + 200) / 2 = 150


def test_category_average_price_empty():
    cat = Category("Пусто", "Нет товаров")
    assert cat.average_price() == 0
