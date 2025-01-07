import unittest

from src.object import Product, Smartphone, LawnGrass, Category


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product(name="Товар 1", description="Описание товара 1", price=100.0, quantity=10)

    def test_initialization(self):
        self.assertEqual(self.product.name, "Товар 1")
        self.assertEqual(self.product.description, "Описание товара 1")
        self.assertEqual(self.product.price, 100.0)
        self.assertEqual(self.product.quantity, 10)

    def test_add_stock(self):
        self.product.add_stock(5)
        self.assertEqual(self.product.quantity, 15)

    def test_add_stock_negative(self):
        with self.assertRaises(ValueError):
            self.product.add_stock(-5)

    def test_price_setter(self):
        self.product.price = 150.0
        self.assertEqual(self.product.price, 150.0)

    def test_price_setter_negative(self):
        with self.assertRaises(ValueError):
            self.product.price = -50.0

    def test_get_info(self):
        info = self.product.get_info()
        self.assertIn("Товар 1", info)
        self.assertIn("100.0", info)
        self.assertIn("10", info)

    def test_repr(self):
        self.assertEqual(repr(self.product), "(name='Товар 1', price=100.0, quantity=10)")

    def test_addition(self):
        other_product = Product(name="Товар 2", description="Описание товара 2", price=200.0, quantity=5)
        total_price = self.product + other_product
        self.assertEqual(total_price, 2000.0)  # (100 * 10) + (200 * 5)

    def test_addition_type_error(self):
        with self.assertRaises(TypeError):
            self.product + "not a product"

    def test_empty_product_repr(self):
        # Создаем продукт с количеством 1, чтобы избежать исключения
        empty_product = Product(name="", description="", price=0.0, quantity=1)
        self.assertEqual(repr(empty_product), "(name='', price=0.0, quantity=1)")

    def test_product_str(self):
        self.assertEqual(str(self.product), "Товар 1, 100.0 руб. Остаток: 10 шт.")


class TestSmartphone(unittest.TestCase):
    def setUp(self):
        self.smartphone = Smartphone(name="Смартфон 1", description="Описание смартфона", price=300.0,
                                     quantity=20, efficiency="Высокая", model="Модель X", memory=128, color="Черный")

    def test_get_info(self):
        info = self.smartphone.get_info()
        self.assertIn("Смартфон 1", info)
        self.assertIn("300.0", info)
        self.assertIn("20", info)
        self.assertIn("эффективность: Высокая", info)
        self.assertIn("модель: Модель X", info)
        self.assertIn("память: 128GB", info)
        self.assertIn("цвет: Черный", info)

    def test_repr(self):
        self.assertIn("Смартфон 1", repr(self.smartphone))
        self.assertIn("(name='Смартфон 1', price=300.0, quantity=20), "
                       "efficiency='Высокая', model='Модель X', memory=128 GB, color='Черный'", repr(self.smartphone))


class TestLawnGrass(unittest.TestCase):
    def setUp(self):
        self.lawn_grass = LawnGrass(name="Газонная трава", description="Описание травы", price=50.0,
                                    quantity=100, country="Россия", germination_period=14, color="Зеленый")

    def test_get_info(self):
        info = self.lawn_grass.get_info()
        self.assertIn("Газонная трава", info)
        self.assertIn("50.0", info)
        self.assertIn("100", info)
        self.assertIn("страна: Россия", info)
        self.assertIn("срок прорастания: 14 дней", info)
        self.assertIn("цвет: Зеленый", info)

    def test_repr(self):
        self.assertIn("Газонная трава", repr(self.lawn_grass))
        self.assertIn("(name='Газонная трава', price=50.0, quantity=100), country='Россия', "
                      "germination_period=14 days, color='Зеленый'", repr(self.lawn_grass))


class TestCategory(unittest.TestCase):
    def setUp(self):
        self.product1 = Product(name="Товар 1", description="Описание товара 1", price=100.0, quantity=10)
        self.product2 = Product(name="Товар 2", description="Описание товара 2", price=200.0, quantity=5)
        self.category = Category(name="Категория 1", description="Описание категории", products=[self.product1, self.product2])

    def test_initialization(self):
        self.assertEqual(self.category.name, "Категория 1")
        self.assertEqual(self.category.description, "Описание категории")
        self.assertEqual(len(self.category._products), 2)

    def test_add_product(self):
        new_product = Product(name="Товар 3", description="Описание товара 3", price=150.0, quantity=20)
        self.category.add_product(new_product)
        self.assertEqual(len(self.category._products), 3)

    def test_add_product_invalid_type(self):
        with self.assertRaises(TypeError):
            self.category.add_product("not a product")

    def test_middle_price(self):
        self.assertEqual(self.category.middle_price(), 150.0)  # (100 + 200) / 2

    def test_middle_price_empty(self):
        empty_category = Category(name="Пустая категория", description="Нет продуктов", products=[])
        self.assertEqual(empty_category.middle_price(), 0)

    def test_str(self):
        self.assertIn("Категория 1", str(self.category))
        self.assertIn("количество продуктов: 15 шт.", str(self.category))

