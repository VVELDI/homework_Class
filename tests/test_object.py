import pytest

from src.object import Product, Category


@pytest.fixture
def reset_category_counts():
    """Фикстура для сброса атрибутов category_count и product_count перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def product_data():
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, "
                                            "Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    ]


@pytest.fixture
def category_data(product_data):
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, "
                    "но и получения дополнительных функций для удобства жизни",
                    product_data)


def test_product_initialization():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, "
                                                  "Серый цвет, 200MP камера", 180000.0, 5)

    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_initialization(category_data):
    category = category_data

    assert category.name == "Смартфоны"
    assert category.description == ("Смартфоны, как средство не только коммуникации, "
                                    "но и получения дополнительных функций для удобства жизни")
    assert len(category.products) == 3
    assert Category.category_count == 1
    assert Category.product_count == 3


def test_category_product_count(reset_category_counts):
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, "
                                                   "Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, "
                                    "Gray space", 210000.0, 8)
    category = Category("Смартфоны", "Описание категории", [product1, product2])

    assert Category.product_count == 2


def test_category_count(reset_category_counts):
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, "
                                                   "Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, "
                                    "Gray space", 210000.0, 8)

    category1 = Category("Смартфоны", "Описание категории", [product1, product2])
    category2 = Category("Телевизоры", "Описание категории", [product1])

    assert Category.category_count == 2
