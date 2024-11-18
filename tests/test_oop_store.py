import pytest

from commerce_cours_oop.oop_store import Product, Smartphone, LawnGrass, Category


def test_product_creation():
    product = Product("Товар", "Описание товара", 1000, 5)
    assert product.name == "Товар"
    assert product.price == 1000
    assert product.quantity == 5

def test_smartphone_creation():
    smartphone = Smartphone("Смартфон", "Описание", 50000, 10, 90, "Модель X", 128, "Чёрный")
    assert smartphone.name == "Смартфон"
    assert smartphone.efficiency == 90
    assert smartphone.model == "Модель X"
    assert smartphone.memory == 128
    assert smartphone.color == "Чёрный"

def test_lawn_grass_creation():
    lawn_grass = LawnGrass("Газонная трава", "Описание", 2000, 5, "Россия", 10, "Зелёный")
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == 10
    assert lawn_grass.color == "Зелёный"

def test_add_product_type_error():
    category = Category("Тестовая категория", "Тестовое описание")
    with pytest.raises(TypeError):
        category.add_product("Не продукт")

def test_add_products_different_types():
    smartphone_1 = Smartphone("Смартфон1", "Описание", 50000, 10, 90, "Модель1", 128, "Чёрный")
    smartphone_2 = Smartphone("Смартфон2", "Описание", 60000, 5, 95, "Модель2", 128, "Белый")
    lawn_grass = LawnGrass("Трава газонная", "Описание", 3000, 20, "Россия", 10, "Зелёный")

    with pytest.raises(TypeError):
        smartphone_1 + lawn_grass
