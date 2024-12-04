import pytest  # Убедитесь, что pytest импортирован

from src.object import Product, Category, Smartphone, LawnGrass


def test_product_creation():
    """Проверяем создание объекта Product."""
    product = Product("Laptop", "Gaming laptop", 1000.0, 5)

    assert product.name == "Laptop"
    assert product.description == "Gaming laptop"
    assert product.price == 1000.0
    assert product.quantity == 5
    assert repr(product) == "(name='Laptop', price=1000.0, quantity=5)"


def test_product_price_setter():
    """Проверяем работу сеттера и геттера для цены."""
    product = Product("Laptop", "Gaming laptop", 1000.0, 5)

    # Проверяем установку корректной цены
    product.price = 1200.0
    assert product.price == 1200.0

    # Проверяем сообщение об ошибке при попытке установить некорректную цену
    product.price = -500.0
    assert product.price == 1200.0  # Цена не должна была измениться


def test_product_class_method():
    """Проверяем создание объекта Product через класс-метод."""
    product_data = {
        "name": "Smartphone",
        "description": "Latest model",
        "price": 800.0,
        "quantity": 3,
    }

    product = Product.new_product(product_data)

    assert product.name == "Smartphone"
    assert product.description == "Latest model"
    assert product.price == 800.0
    assert product.quantity == 3


def test_product_addition_with_invalid_type():
    """Проверяем выброс исключения при попытке сложения с объектом другого типа."""
    product = Product("Laptop", "Gaming laptop", 1000.0, 5)

    # Попытка сложения с объектом другого типа
    with pytest.raises(TypeError, match="Операция сложения возможна только между объектами класса Product."):
        result = product + "Not a Product"


def test_product_addition():
    """Проверяем работу метода сложения __add__ между объектами Product."""
    product1 = Product("Laptop", "Gaming laptop", 1000.0, 5)
    product2 = Product("Smartphone", "Latest model", 800.0, 3)

    result = product1 + product2

    # Проверяем, что результат корректен
    assert result == (1000.0 * 5) + (800.0 * 3)  # 5000 + 2400 = 7400


def test_category_creation():
    """Проверяем создание объекта Category и обновление атрибутов класса."""
    # Сбросим атрибуты класса перед тестами
    Category.category_count = 0
    Category.product_count = 0

    # Создаем категорию
    category = Category("Electronics", "Electronic devices", [])

    assert category.name == "Electronics"
    assert category.description == "Electronic devices"
    assert Category.category_count == 1
    assert Category.product_count == 0  # Список продуктов изначально пуст
    assert str(category) == "Electronics, количество продуктов: 0 шт."

    # Создаем продукты и добавляем их в категорию
    product1 = Product("Laptop", "Gaming laptop", 1000.0, 5)
    product2 = Product("Smartphone", "Latest model", 800.0, 3)

    category.add_product(product1)
    category.add_product(product2)

    # Проверяем обновление приватного списка и счетчика продуктов
    assert Category.product_count == 2
    assert category.products == (
        "Laptop, 1000.0 руб. Остаток: 5 шт.\n"
        "Smartphone, 800.0 руб. Остаток: 3 шт.\n"
    )


def test_smartphone_creation():
    """Проверяем создание объекта Smartphone и его представление."""
    smartphone = Smartphone(
        name="iPhone",
        description="Latest iPhone model",
        price=1200.0,
        quantity=10,
        efficiency="High",
        model="iPhone 15 Pro",
        memory=256,
        color="Black"
    )

    assert smartphone.name == "iPhone"
    assert smartphone.description == "Latest iPhone model"
    assert smartphone.price == 1200.0
    assert smartphone.quantity == 10
    assert smartphone.efficiency == "High"
    assert smartphone.model == "iPhone 15 Pro"
    assert smartphone.memory == 256
    assert smartphone.color == "Black"
    assert repr(smartphone) == (
        "(name='iPhone', price=1200.0, quantity=10), "
        "efficiency='High', model='iPhone 15 Pro', memory=256 GB, color='Black'"
    )


def test_lawngrass_creation():
    """Проверяем создание объекта LawnGrass и его представление."""
    lawn_grass = LawnGrass(
        name="Premium Grass",
        description="High-quality lawn grass",
        price=200.0,
        quantity=50,
        country="Netherlands",
        germination_period=30,
        color="Green"
    )

    assert lawn_grass.name == "Premium Grass"
    assert lawn_grass.description == "High-quality lawn grass"
    assert lawn_grass.price == 200.0
    assert lawn_grass.quantity == 50
    assert lawn_grass.country == "Netherlands"
    assert lawn_grass.germination_period == 30
    assert lawn_grass.color == "Green"
    assert repr(lawn_grass) == (
        "(name='Premium Grass', price=200.0, quantity=50), "
        "country='Netherlands', germination_period=30 days, color='Green'"
    )


def test_category_with_different_products():
    """Проверяем работу класса Category с разными типами продуктов."""
    Category.category_count = 0
    Category.product_count = 0

    # Создаем продукты
    smartphone = Smartphone(
        name="Galaxy S22",
        description="Samsung flagship",
        price=1000.0,
        quantity=15,
        efficiency="High",
        model="Galaxy S22 Ultra",
        memory=512,
        color="Blue"
    )
    lawn_grass = LawnGrass(
        name="Eco Lawn",
        description="Eco-friendly lawn grass",
        price=150.0,
        quantity=100,
        country="USA",
        germination_period=45,
        color="Bright Green"
    )

    # Создаем категорию и добавляем продукты
    category = Category("Mixed Goods", "Smartphones and Lawn Grass", [])
    category.add_product(smartphone)
    category.add_product(lawn_grass)

    # Проверяем свойства категории
    assert Category.category_count == 1
    assert Category.product_count == 2
    assert str(category) == "Mixed Goods, количество продуктов: 115 шт."
    assert category.products == (
        "Galaxy S22, 1000.0 руб. Остаток: 15 шт.\n"
        "Eco Lawn, 150.0 руб. Остаток: 100 шт.\n"
    )
