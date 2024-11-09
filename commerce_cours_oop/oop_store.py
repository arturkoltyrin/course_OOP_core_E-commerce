class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут для цены
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для установки цены."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    def __repr__(self):
        return (
            f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"
        )

    @classmethod
    def new_product(cls, product_info, existing_products):
        """Создание нового продукта или добавление к существующему."""
        name = product_info["name"]
        price = product_info["price"]
        description = product_info["description"]
        quantity = product_info["quantity"]

        # Проверка на дубликаты
        for existing_product in existing_products:
            if existing_product.name == name:
                existing_product.quantity += quantity
                if price > existing_product.price:
                    existing_product.price = price
                return existing_product  # Возвращаем существующий продукт

        # Если продукт не найден, создаем новый
        return cls(name, description, price, quantity)


class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__products = []  # Приватный атрибут для списка продуктов

        # Увеличиваем количество категорий
        Category.total_categories += 1

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.total_products += 1

    @property
    def products(self):
        """Геттер для получения списка продуктов в строковом формате."""
        return "\n".join(
            [
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
                for product in self.__products
            ]
        )

    def __repr__(self):
        return f"Category(name={self.name}, total_products={len(self.__products)})"
