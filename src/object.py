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
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        """
        Возвращает строковое представление объекта Product.
        """
        return (f"(name='{self.name}', "
                f"price={self.price}, "
                f"quantity={self.quantity})")


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
        self.products = products

        # Увеличиваем счетчики категорий и продуктов
        Category.category_count += 1
        Category.product_count += len(products)
