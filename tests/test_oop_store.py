import pytest

from commerce_cours_oop.oop_store import Smartphone, LawnGrass, Category


def test_smartphone_creation():
    smartphone = Smartphone(
        name="iPhone 13",
        description="Смартфон от Apple с отличной камерой",
        price=799.99,
        quantity=10,
        efficiency=5.0,
        model="A2634",
        memory=256,
        color="синий",
    )
    assert smartphone.name == "iPhone 13"
    assert smartphone.price == 799.99
    assert smartphone.quantity == 10


# Тесты для класса LawnGrass
def test_lawn_grass_creation():
    lawn_grass = LawnGrass(
        name="Газонная трава ЛУГА",
        description="Смесь трав для газонов",
        price=25.5,
        quantity=50,
        country="Россия",
        germination_period=14,
        color="зеленый",
    )
    assert lawn_grass.name == "Газонная трава ЛУГА"
    assert lawn_grass.price == 25.5
    assert lawn_grass.country == "Россия"


# Тесты для класса Category
def test_category_add_product():
    category = Category("Электроника", "Все подкатегории электроники")

    smartphone = Smartphone(
        name="iPhone 13",
        description="Смартфон от Apple с отличной камерой",
        price=799.99,
        quantity=10,
        efficiency=5.0,
        model="A2634",
        memory=256,
        color="синий",
    )

    category.add_product(smartphone)
    assert len(category.products.split("\n")) == 1
    assert "iPhone 13" in category.products
