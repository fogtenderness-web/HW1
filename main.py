from src.models import Product, Category

def main():
    # Создаём несколько товаров
    milk = Product("Молоко", "1 литр, 3.2%", 89.99, 15)
    bread = Product("Хлеб", "Ржаной, нарезка", 54.50, 30)

    # Создаём категорию и добавляем товары
    groceries = Category("Бакалея", "Продукты первой необходимости", [milk, bread])

    # Можно добавить ещё товар после создания категории
    eggs = Product("Яйца", "10 штук, С0", 109.90, 20)
    groceries.products.append(eggs)

    # Выведем информацию
    print(f"Категория: {groceries.name}")
    print(f"Описание: {groceries.description}")
    print("Товары:")
    for product in groceries.products:
        print(f"  - {product.name}: {product.price} руб. (в наличии: {product.quantity} шт.)")

if __name__ == "__main__":
    main()