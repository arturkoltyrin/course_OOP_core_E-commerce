import json
import os

from oop_store import Category, Product


def load_data_from_json(file_name: str):
    # Получаем полный путь к файлу
    file_path = os.path.join(os.path.dirname(__file__), "..", "data", file_name)

    # Читаем данные из JSON-файла
    with open(file_path, "r") as f:
        data = json.load(f)

    categories = []

    # Итерируемся по каждой категории в загруженных данных
    for category_data in data:
        category = Category(
            name=category_data["name"], description=category_data["description"]
        )

        # Итерируемся по продуктам в каждой категории
        for product_data in category_data.get("products", []):
            product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                quantity=product_data["quantity"],
            )
            category.add_product(product)  # Добавляем продукт в категорию

        categories.append(category)  # Добавляем категорию в общий список

    return categories


if __name__ == "__main__":
    categories = load_data_from_json("../data/products.json")
