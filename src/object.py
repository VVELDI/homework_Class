from abc import ABC, abstractmethod


# Базовый абстрактный класс для всех продуктов
class BaseProduct(ABC):
    @abstractmethod
    def get_info(self):
        """Метод для получения информации о продукте"""
        pass

    @property
    @abstractmethod
    def price(self):
        """Свойство для доступа к цене продукта"""
        pass

    @abstractmethod
    def add_stock(self, amount: int):
        """Метод для добавления товаров на склад"""
        pass


# Класс-миксин, который выводит информацию о создании объекта
class CreationLogMixin:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        class_name = self.__class__.__name__
        print(
            f"Создание {class_name} с параметрами: name='{name}', description='{description}', price={price}, quantity={quantity}")
        super().__init__()


# Класс Product, который наследует от BaseProduct и включает миксин
class Product(BaseProduct, CreationLogMixin):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен.")
        else:
            super().__init__(name, description, price, quantity)
            self.__price = price  # Цена становится приватной
            self.quantity = quantity
            self.name = name
            self.description = description

    def __repr__(self):
        return (f"(name='{self.name}', "
                f"price={self.__price}, "
                f"quantity={self.quantity})")

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Операция сложения возможна только между объектами класса Product.")
        return (self.__price * self.quantity) + (other.__price * other.quantity)

    @classmethod
    def new_product(cls, data: dict):
        return cls(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            quantity=data['quantity']
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")  # Изменено на выброс исключения
        self.__price = value

    def get_info(self):
        return f"Продукт: {self.name}, цена: {self.__price}, количество: {self.quantity}"

    def add_stock(self, amount: int):
        if amount <= 0:
            raise ValueError("Количество добавляемого товара должно быть положительным.")
        self.quantity += amount


# Класс Smartphone, наследующий от Product
class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float,
                 quantity: int, efficiency: str, model: str,
                 memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __repr__(self):
        return (super().__repr__() +
                f", efficiency='{self.efficiency}', model='{self.model}', "
                f"memory={self.memory} GB, color='{self.color}'")

    def get_info(self):
        return (super().get_info() +
                f", эффективность: {self.efficiency}, модель: {self.model}, "
                f"память: {self.memory}GB, цвет: {self.color}")


# Класс LawnGrass, наследующий от Product
class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float,
                 quantity: int, country: str, germination_period: int,
                 color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __repr__(self):
        return (super().__repr__() +
                f", country='{self.country}', germination_period={self.germination_period} days, color='{self.color}'")

    def get_info(self):
        return (super().get_info() +
                f", страна: {self.country}, срок прорастания: {self.germination_period} дней, "
                f"цвет: {self.color}")


# Класс Category для управления продуктами
class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self._products = []  # Приватный список продуктов

        # Добавление продуктов через метод, чтобы применить проверки
        for product in products:
            self.add_product(product)

        Category.category_count += 1

    def __str__(self):
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников.")
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return "\n".join(str(product) for product in self._products) + "\n"

    def middle_price(self):
        """Метод для подсчета средней цены товаров в категории."""
        if not self._products:  # Проверка на пустой список
            return 0
        total_price = sum(product.price for product in self._products)
        return total_price / len(self._products)
