import pytest

from commerce_cours_oop.oop_store import Category, Product


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
