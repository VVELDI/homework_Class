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
        self.__price = price  # Цена становится приватной
        self.quantity = quantity

    def __repr__(self):
        """
        Возвращает строковое представление объекта Product.
        """
        return (f"(name='{self.name}', "
                f"price={self.__price}, "
                f"quantity={self.quantity})")

    def __str__(self):
        """
        Строковое представление продукта в формате:
        'Название продукта, 80 руб. Остаток: 15 шт.'
        """
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Реализация сложения для продуктов.
        Сумма равна общей стоимости всех товаров.
        """
        if not isinstance(other, Product):
            raise TypeError("Операция сложения возможна только между объектами класса Product.")
        return (self.__price * self.quantity) + (other.__price * other.quantity)

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
        return self.__price

    @price.setter
    def price(self, value: float):
        """
        Сеттер для установки значения цены с проверкой.
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value


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

    def __str__(self):
        """
        Строковое представление категории в формате:
        'Название категории, количество продуктов: 200 шт.'
        """
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product):
        """
        Метод для добавления продукта в категорию.

        :param product: Объект класса Product
        """
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return "\n".join(str(product) for product in self._products) + "\n"
