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
        return (f"(name='{self.name}', "
                f"price={self.__price}, "
                f"quantity={self.quantity})")

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Сложение возможно только между объектами одного типа.")
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
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: str, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __repr__(self):
        return (super().__repr__() +
                f", efficiency='{self.efficiency}', model='{self.model}', memory={self.memory} GB, color='{self.color}'")


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: int, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __repr__(self):
        return (super().__repr__() +
                f", country='{self.country}', germination_period={self.germination_period} days, color='{self.color}'")


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
