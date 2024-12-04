# Проект: Управление продуктами и категориями

## Описание

В данном проекте реализованы классы для работы с продуктами и их категориями. Класс **`Product`** описывает отдельный 
продукт, а **`Category`** — категории, содержащие несколько продуктов.

### **Product**

Класс для представления информации о продукте.

#### Параметры конструктора:
- **`name (str)`** — Название продукта.  
- **`description (str)`** — Описание продукта.  
- **`price (float)`** — Цена продукта.  
- **`quantity (int)`** — Количество доступного товара.  

#### Методы:
- **`__repr__()`** — Возвращает строковое представление объекта.
- **`__str__()`** — Строковое представление объекта в читаемом формате.
- **`__add__()`** — Реализует сложение продуктов с одинаковыми классами (суммирует стоимость всех единиц товара).
- **`new_product()`** — Класс-метод для создания нового продукта на основе словаря данных.
- **`price (property)`** — Свойство для работы с ценой товара, с возможностью установки значений через setter.

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
### 3. Класс **`Smartphone`**

```markdown
### **Smartphone**

Класс-наследник **`Product`**, расширяющий функционал и добавляющий следующие атрибуты:
- **`efficiency (str)`** — Производительность устройства.  
- **`model (str)`** — Модель устройства.  
- **`memory (int)`** — Объем встроенной памяти (в ГБ).  
- **`color (str)`** — Цвет устройства.

#### Пример использования:
```python
from src.object import Smartphone

smartphone = Smartphone(
    "iPhone 14", 
    "Latest Apple smartphone", 
    1200.0, 
    10, 
    "High", 
    "iPhone 14", 
    256, 
    "Black"
)
print(smartphone)  # iPhone 14, 1200.0 руб. Остаток: 10 шт.
print(repr(smartphone))  # (name='iPhone 14', price=1200.0, quantity=10, efficiency='High', model='iPhone 14', memory=256, color='Black')
```


### 4. Класс **`LawnGrass`**

```markdown
### **LawnGrass**

Класс-наследник **`Product`**, расширяющий функционал и добавляющий следующие атрибуты:
- **`country (str)`** — Страна-производитель.  
- **`germination_period (int)`** — Срок прорастания (в днях).  
- **`color (str)`** — Цвет травы.

#### Пример использования:
```python
from src.object import LawnGrass

grass = LawnGrass(
    "Premium Lawn", 
    "High-quality lawn grass", 
    500.0, 
    20, 
    "USA", 
    10, 
    "Green"
)
print(grass)  # Premium Lawn, 500.0 руб. Остаток: 20 шт.
print(repr(grass))  # (name='Premium Lawn', price=500.0, quantity=20, country='USA', germination_period=10, color='Green')
```


### 5. Класс **`Category`**

```markdown
### **Category**

Класс для представления категории, которая объединяет несколько продуктов.

#### Атрибуты класса:
- **`category_count`** — Количество созданных категорий.
- **`product_count`** — Общее количество продуктов во всех категориях.

#### Параметры конструктора:
- **`name (str)`** — Название категории.
- **`description (str)`** — Описание категории.
- **`products (list[Product])`** — Список продуктов, относящихся к категории.

#### Методы:
- **`add_product()`** — Метод для добавления продуктов в категорию с проверкой, что добавляемый объект является экземпляром класса **`Product`** или его наследников.
- **`products`** — Свойство для получения списка всех продуктов в категории в строковом формате.

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

### 6. Тестирование

```markdown
## Тестирование

### Установка и запуск:

1. Установите pytest (если он ещё не установлен):

```bash
pip install pytest
```
Запустите тесты:
```bash
pytest
```

### 7. Структура проекта

```markdown
## Структура проекта
project/ ├── src/ │── object.py # Основные классы 
         ├──      ├── main.py # Основной модуль для работы с классами
         ├── tests/test_object.py # Тесты для объектов 
         └── README.md # Описание проекта
