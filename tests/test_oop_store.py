import pytest
from commerce_cours_oop.oop_store import Product, Category


def test_product_initialization():
    product = Product(
        name="Laptop", description="A high-performing laptop", price=999.99, quantity=10
    )
    assert product.name == "Laptop"
    assert product.description == "A high-performing laptop"
    assert product.price == 999.99
    assert product.quantity == 10


def test_category_initialization():
    category = Category(name="Electronics", description="All electronic items")
    assert category.name == "Electronics"
    assert category.description == "All electronic items"
    assert len(category.products) == 0


def test_product_count():
    category = Category(name="Electronics", description="All electronic items")
    product1 = Product(
        name="Laptop", description="A high-performing laptop", price=999.99, quantity=10
    )
    product2 = Product(
        name="Smartphone",
        description="A smartphone with great features",
        price=499.99,
        quantity=20,
    )
    category.add_product(product1)
    category.add_product(product2)
    assert len(category.products) == 2
    assert Category.total_products == 2
