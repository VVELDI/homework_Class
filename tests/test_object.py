from src.object import Product, Category


def test_product_creation():
    """Проверяем создание объекта Product."""
    product = Product("Laptop", "Gaming laptop", 1000.0, 5)

    assert product.name == "Laptop"
    assert product.description == "Gaming laptop"
    assert product.price == 1000.0
    assert product.quantity == 5
    assert repr(product) == "(name='Laptop', price=1000.0, quantity=5)"


def test_category_creation():
    """Проверяем создание объекта Category и обновление атрибутов класса."""
    # Сбросим атрибуты класса перед тестами
    Category.category_count = 0
    Category.product_count = 0

    # Создаем продукты
    product1 = Product("Laptop", "Gaming laptop", 1000.0, 5)
    product2 = Product("Smartphone", "Latest model", 800.0, 3)

    # Создаем категории
    category1 = Category("Electronics", "Electronic devices", [product1, product2])

    assert category1.name == "Electronics"
    assert category1.description == "Electronic devices"
    assert len(category1.products) == 2
    assert Category.category_count == 1  # Одна категория
    assert Category.product_count == 2  # Два продукта

    # Проверяем создание второй категории
    product3 = Product("Tablet", "High-performance tablet", 500.0, 2)
    category2 = Category("Gadgets", "Portable devices", [product3])

    assert category2.name == "Gadgets"
    assert category2.description == "Portable devices"
    assert len(category2.products) == 1
    assert Category.category_count == 2  # Две категории
    assert Category.product_count == 3  # Всего три продукта
