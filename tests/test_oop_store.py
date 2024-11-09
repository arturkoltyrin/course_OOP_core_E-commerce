import pytest

from commerce_cours_oop.oop_store import Category, Product


def test_product_initialization():
    product = Product("Телевизор", "4K UHD", 8000, 10)
    assert product.name == "Телевизор"
    assert product.description == "4K UHD"
    assert product.price == 8000
    assert product.quantity == 10


def test_product_price_setter_valid():
    product = Product("Телевизор", "4K UHD", 8000, 10)
    product.price = 7500
    assert product.price == 7500


def test_product_price_setter_invalid():
    product = Product("Телевизор", "4K UHD", 8000, 10)
    product.price = -100  # Должен вывести сообщение об ошибке
    assert product.price == 8000  # Цена не изменилась


def test_product_new_product_creation():
    existing_products = []
    product_info = {
        "name": "Смартфон",
        "description": "Android phone",
        "price": 5000,
        "quantity": 20,
    }

    new_product = Product.new_product(product_info, existing_products)
    assert new_product.name == "Смартфон"
    assert new_product.quantity == 20

    # Проверка дублирования
    existing_product_info = {
        "name": "Смартфон",
        "description": "New Android phone",
        "price": 6000,
        "quantity": 10,
    }

    existing_products.append(new_product)
    updated_product = Product.new_product(existing_product_info, existing_products)

    # Обновление quantities и price
    assert updated_product.quantity == 30  # 20 + 10
    assert updated_product.price == 6000  # Должен взять более высокую цену


def test_category_initialization():
    category = Category("Электроника", "Все, что связано с электроникой")
    assert category.name == "Электроника"
    assert category.description == "Все, что связано с электроникой"
    assert len(category.products) == 0


def test_category_products_property():
    category = Category("Электроника", "Все, что связано с электроникой")
    product1 = Product("Телевизор", "4K UHD", 8000, 10)
    product2 = Product("Смартфон", "Android phone", 5000, 20)

    category.add_product(product1)
    category.add_product(product2)

    expected_output = (
        "Телевизор, 8000 руб. Остаток: 10 шт.\nСмартфон, 5000 руб. Остаток: 20 шт."
    )
    assert category.products == expected_output
