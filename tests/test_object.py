import pytest
from src.object import Product, Smartphone, LawnGrass, Category


# Фикстуры для создания объектов
@pytest.fixture
def product():
    return Product("Тестовый продукт", "Описание тестового продукта", 100.0, 50)


@pytest.fixture
def smartphone():
    return Smartphone("Тестовый смартфон",
                      "Описание смартфона", 300.0, 20, "High",
                      "Model X", 128, "Black")


@pytest.fixture
def lawn_grass():
    return LawnGrass("Тестовый газон",
                     "Описание газона",
                     50.0, 100, "Россия", 14, "Зеленый")


@pytest.fixture
def category(product, smartphone):
    return Category("Тестовая категория",
                    "Описание категории", [product, smartphone])


def test_product_initialization(product):
    """Проверяем инициализацию объекта Product"""
    assert product.name == "Тестовый продукт"
    assert product.description == "Описание тестового продукта"
    assert product.price == 100.0
    assert product.quantity == 50


def test_smartphone_initialization(smartphone):
    """Проверяем инициализацию объекта Smartphone"""
    assert smartphone.name == "Тестовый смартфон"
    assert smartphone.efficiency == "High"
    assert smartphone.memory == 128
    assert smartphone.color == "Black"


def test_lawn_grass_initialization(lawn_grass):
    """Проверяем инициализацию объекта LawnGrass"""
    assert lawn_grass.name == "Тестовый газон"
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == 14
    assert lawn_grass.color == "Зеленый"


def test_product_get_info(product):
    """Проверяем метод get_info для Product"""
    expected_info = "Продукт: Тестовый продукт, цена: 100.0, количество: 50"
    assert product.get_info() == expected_info


def test_smartphone_get_info(smartphone):
    """Проверяем метод get_info для Smartphone"""
    expected_info = ("Продукт: Тестовый смартфон, цена: 300.0, количество: 20, "
                     "эффективность: High, модель: Model X, память: 128GB, цвет: Black")
    assert smartphone.get_info() == expected_info


def test_lawn_grass_get_info(lawn_grass):
    """Проверяем метод get_info для LawnGrass"""
    expected_info = ("Продукт: Тестовый газон, цена: 50.0, количество: 100, "
                     "страна: Россия, срок прорастания: 14 дней, цвет: Зеленый")
    assert lawn_grass.get_info() == expected_info


def test_product_add_stock(product):
    """Проверяем метод add_stock"""
    product.add_stock(10)
    assert product.quantity == 60


def test_product_add_stock_negative(product):
    """Проверяем метод add_stock на отрицательное значение"""
    product.add_stock(-5)
    assert product.quantity == 50  # Количество должно остаться прежним


def test_product_initialization_zero_quantity():
    """Проверяем инициализацию объекта Product с нулевым количеством"""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен."):
        Product("Бракованный товар", "Неверное количество", 100.0, 0)  # Ожидаем исключение


def test_product_price_setter(product):
    """Проверяем установку цены через сеттер"""
    product.price = 200.0
    assert product.price == 200.0


def test_product_price_setter_negative(product):
    """Проверяем установку отрицательной цены"""
    product.price = -50.0
    assert product.price == 100.0  # Цена должна остаться прежней


def test_category_initialization(category):
    """Проверяем инициализацию объекта Category"""
    assert category.name == "Тестовая категория"
    assert category.description == "Описание категории"
    assert len(category._products) == 2  # Два продукта уже добавлено


def test_category_add_product(product, category):
    """Проверяем добавление продукта в категорию"""
    new_product = Product("Новый продукт", "Описание нового продукта", 150.0, 15)
    category.add_product(new_product)
    assert len(category._products) == 3  # Три продукта теперь в категории


def test_category_add_invalid_product(category):
    """Проверяем добавление невалидного продукта"""
    with pytest.raises(TypeError):
        category.add_product("Некорректный продукт")  # Ожидаем исключение


def test_category_middle_price(category):
    """Проверяем расчет средней цены в категории"""
    assert category.middle_price() == 200.0  # (100 + 300) / 2 = 200


def test_category_middle_price_empty():
    """Проверяем расчет средней цены в пустой категории"""
    empty_category = Category("Пустая категория", "Категория без продуктов", [])
    assert empty_category.middle_price() == 0  # Ожидаем 0 для пустой категории


def test_product_addition_raises_error_for_non_product():
    """Проверяем, что возникает ошибка при добавлении не продукта"""
    category = Category("Тестовая категория", "Описание категории", [])
    with pytest.raises(TypeError):
        category.add_product(None)  # Ожидаем исключение


def test_product_addition_success(product):
    """Проверяем, что продукт добавляется в категорию успешно"""
    category = Category("Тестовая категория", "Описание категории", [])
    category.add_product(product)
    assert len(category._products) == 1
