import pytest

from commerce_cours_oop.oop_store import Category, Product, Smartphone, LawnGrass, Order


def test_product_creation():
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product("Тест", "Описание", 100.0, 0)


def test_category_average_price():
    category = Category("Тестовая категория", "Описание категории")
    product1 = Product("Товар 1", "Описание 1", 100.0, 10)
    product2 = Product("Товар 2", "Описание 2", 200.0, 5)
    category.add_product(product1)
    category.add_product(product2)
    assert category.average_price() == 150.0

    # Проверка для пустой категории
    empty_category = Category("Пустая категория", "Пусто")
    assert empty_category.average_price() == 0


def test_product_creation_zero_quantity():
    with pytest.raises(ValueError):
        Product("Test Product", "Test Description", 10.0, 0)

def test_product_price_setter():
    product = Product("Test Product", "Test Description", 10.0, 5)
    product.price = 15.0
    assert product.price == 15.0

def test_product_repr():
    product = Product("Test Product", "Test Description", 10.0, 5)
    assert repr(product) == "Product(name=Test Product, price=10.0, quantity=5)"

def test_product_add():
    product1 = Product("Test Product", "Test Description", 10.0, 5)
    product2 = Product("Test Product", "Test Description", 10.0, 3)
    product3 = product1 + product2
    assert product3.quantity == 8
    assert repr(product3) == "Product(name=Test Product, price=10.0, quantity=8)"

def test_product_add_different_types():
    product1 = Product("Test Product", "Test Description", 10.0, 5)

    class AnotherProduct(Product): pass

    product2 = AnotherProduct("Test Product", "Test Description", 10.0, 5)
    with pytest.raises(TypeError):
        product1 + product2

# Тест для Smartphone
def test_smartphone_creation():
    product_info = {
        "name": "Smartphone X",
        "description": "Awesome phone",
        "price": 1000.00,
        "quantity": 10,
        "efficiency": 0.9,
        "model": "XYZ123",
        "memory": 128,
        "color": "Black",
    }
    smartphone = Smartphone.new_product(product_info)
    assert smartphone.name == "Smartphone X"
    assert smartphone.efficiency == 0.9
    assert smartphone.model == "XYZ123"


def test_smartphone_creation_with_negative_quantity():
    product_info = {
        "name": "Smartphone X",
        "description": "Awesome phone",
        "price": 1000.00,
        "quantity": -5,
        "efficiency": 0.9,
        "model": "XYZ123",
        "memory": 128,
        "color": "Black",
    }
    with pytest.raises(ValueError):
        Smartphone.new_product(product_info)

@pytest.fixture
def category():
    return Category("Electronics", "Electronic devices")

@pytest.fixture
def product():
    return Product("Test Product", "Test Description", 10.0, 5)

def test_category_creation():
    category = Category("Electronics", "Electronic devices")
    assert category.name == "Electronics"
    assert category.description == "Electronic devices"
    assert len(category._Category__products) == 0

def test_average_price_empty(category):
    assert category.average_price() == 0


def test_average_price(category, product):
    category.add_product(product)
    assert category.average_price() == 10.0

def test_products_property(category, product):
    category.add_product(product)
    assert "Test Product, 10.0 руб. Остаток: 5 шт." in category.products

def test_repr(category, product):
    category.add_product(product)
    assert repr(category) == "Category(name=Electronics, total_products=1)"

# Тесты для LawnGrass
def test_lawngrass_creation_missing_key():
    product_info = {
        "name": "Festuca",
        "description": "High-quality lawn grass",
        "price": 25.0,
        "quantity": 10,
        "country": "Netherlands",
        "germination_period": 14,
    }
    with pytest.raises(KeyError):
        LawnGrass.new_product(product_info)

def test_lawngrass_creation():
    lawngrass = LawnGrass("Festuca", "High-quality lawn grass", 25.0, 10, "Netherlands", 14, "Green")
    assert lawngrass.name == "Festuca"
    assert lawngrass.description == "High-quality lawn grass"
    assert lawngrass.price == 25.0
    assert lawngrass.quantity == 10
    assert lawngrass.country == "Netherlands"
    assert lawngrass.germination_period == 14
    assert lawngrass.color == "Green"

def test_lawngrass_creation_zero_quantity():
    with pytest.raises(ValueError) as excinfo:
        LawnGrass("Festuca", "High-quality lawn grass", 25.0, 0, "Netherlands", 14, "Green")
    assert "Товар с нулевым количеством не может быть добавлен" in str(excinfo.value)

def test_lawngrass_creation_negative_quantity():
    with pytest.raises(ValueError) as excinfo:
        LawnGrass("Festuca", "High-quality lawn grass", 25.0, -5, "Netherlands", 14, "Green")
    assert "Товар с нулевым количеством не может быть добавлен" in str(excinfo.value)


def test_lawngrass_from_dict():
    product_info = {
        "name": "Festuca",
        "description": "High-quality lawn grass",
        "price": 25.0,
        "quantity": 10,
        "country": "Netherlands",
        "germination_period": 14,
        "color": "Green",
    }
    lawngrass = LawnGrass.new_product(product_info)
    assert lawngrass.name == "Festuca"
    assert lawngrass.description == "High-quality lawn grass"
    assert lawngrass.price == 25.0
    assert lawngrass.quantity == 10
    assert lawngrass.country == "Netherlands"
    assert lawngrass.germination_period == 14
    assert lawngrass.color == "Green"


def test_lawngrass_from_dict_missing_key():
    product_info = {
        "name": "Festuca",
        "description": "High-quality lawn grass",
        "price": 25.0,
        "quantity": 10,
        "country": "Netherlands",
        "germination_period": 14,
    }
    with pytest.raises(KeyError):
        LawnGrass.new_product(product_info)

def test_category_average_price_with_zero_price_product(category, product):
    product_zero_price = Product("Zero Price Product", "Description", 0, 1)
    category.add_product(product)
    category.add_product(product_zero_price)
    assert category.average_price() == product.price / 2

def test_smartphone_creation_with_edge_cases():
    max_memory = 1024*1024*1024*2
    smartphone = Smartphone("Large phone", "Big Description", 2000.00, 1, 0.98, "BigModel", max_memory, "Green")
    assert smartphone.memory == max_memory

def test_order_creation(product):
    order = Order(product, 2)
    assert order.product == product
    assert order.quantity == 2
    assert order.total_price == 20.0
    assert repr(order) == "Order(product=Test Product, quantity=2, total_price=20.0)"

def test_order_repr_with_different_values(product):
    order = Order(product, 5)
    assert repr(order) == "Order(product=Test Product, quantity=5, total_price=50.0)"


# Example test cases, replace with your actual scenarios
def test_order_creation_with_large_quantity(product):
    order = Order(product, 10)
    assert order.quantity == 10
    assert order.total_price == 100