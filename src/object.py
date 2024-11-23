# src/objects.py

class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Класс описывает продукт.

        :param name: Название продукта
        :param description: Описание продукта
        :param price: Цена продукта
        :param quantity: Количество в наличии
        """
        self.name = name
        self.description = description
        self._price = price  # Цена становится приватной
        self.quantity = quantity

    def __repr__(self):
        """
        Возвращает строковое представление объекта Product.
        """
        return (f"(name='{self.name}', "
                f"price={self._price}, "
                f"quantity={self.quantity})")

    @classmethod
    def new_product(cls, data: dict):
        """
        Класс-метод для создания объекта Product из словаря.

        :param data: Словарь с параметрами товара
        :return: Объект класса Product
        """
        return cls(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            quantity=data['quantity']
        )

    @property
    def price(self):
        """
        Геттер для получения значения цены.
        """
        return self._price

    @price.setter
    def price(self, value: float):
        """
        Сеттер для установки значения цены с проверкой.
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value


class Category:
    # Атрибуты класса для хранения общего количества категорий и продуктов
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """
        Класс описывает категорию.

        :param name: Название категории
        :param description: Описание категории
        :param products: Список продуктов, принадлежащих категории
        """
        self.name = name
        self.description = description
        self._products = products  # Список продуктов становится приватным

        # Увеличиваем общий счетчик категорий
        Category.category_count += 1

        # Увеличиваем общий счетчик продуктов
        Category.product_count += len(products)

    def add_product(self, product: Product):
        """
        Метод для добавления продукта в категорию.

        :param product: Объект класса Product
        """
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """
        Геттер для получения списка товаров категории.

        :return: Строковое представление списка товаров
        """
        return '\n'.join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self._products
        )
