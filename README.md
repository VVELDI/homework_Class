# Проект: Управление продуктами и категориями

## Описание

В данном проекте реализованы классы для работы с продуктами и их категориями. Класс **`Product`** описывает отдельный продукт, а **`Category`** — категории, содержащие несколько продуктов.

---
## Классы

### **Product**

Класс для представления информации о продукте.

#### Параметры конструктора:
- **`name (str)`** — Название продукта.  
- **`description (str)`** — Описание продукта.  
- **`price (float)`** — Цена продукта.  
- **`quantity (int)`** — Количество доступного товара.  

#### Методы:
- **`__repr__()`** — Возвращает строковое представление объекта.

#### Пример использования:
```python
from src.object import Product

product = Product("Laptop", "Gaming laptop", 1000.0, 5)
print(product.name)           # Laptop
print(product.description)    # Gaming laptop
print(product.price)          # 1000.0
print(product.quantity)       # 5
print(repr(product))          # (name='Laptop', price=1000.0, quantity=5)

```

### **Category**

Класс для представления категории, которая объединяет несколько продуктов.

#### Атрибуты класса:
- **`category_count`** — Количество созданных категорий.
- **`product_count`** — Общее количество продуктов во всех категориях.

#### Параметры конструктора:
- **`name (str)`** — Название категории.
- **`description (str)`** — Описание категории.
- **`products (list[Product])`** — Список продуктов, относящихся к категории.

#### Пример использования:
```python
from src.object import Product, Category

# Создание продуктов
product1 = Product("Laptop", "Gaming laptop", 1000.0, 5)
product2 = Product("Smartphone", "Latest model", 800.0, 3)

# Создание категории
category = Category("Electronics", "Electronic devices", [product1, product2])

print(category.name)              # Electronics
print(category.description)       # Electronic devices
print(len(category.products))     # 2
print(Category.category_count)    # 1
print(Category.product_count)     # 2
```
## Тестирование

### Установка и запуск:

1. Установите pytest (если он ещё не установлен):

```bash
pip install pytest
```

## Структура проекта

```
project/
├── src/
│   └── object.py           # Основные классы
├── tests/
│   └── test_object.py      # Тесты для объектов
└── README.md                # Описание проекта
```