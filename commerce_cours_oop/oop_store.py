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

    def __str__(self):
        """Строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Суммирование полной стоимости двух товаров."""
        if isinstance(other, Product):
            return (self.price * self.quantity) + (other.price * other.quantity)
        return NotImplemented

    @classmethod
    def new_product(cls, product_info):
        """Создание нового продукта."""
        name = product_info["name"]
        price = product_info["price"]
        description = product_info["description"]
        quantity = product_info["quantity"]
        return cls(name, description, price, quantity)


class Category:
    total_categories = 0
    product_count = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__products = []  # Приватный атрибут для списка продуктов
        Category.total_categories += 1

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1  # Исправил замечание на product_count

    @property
    def products(self):
        """Геттер для получения списка продуктов в строковом формате."""
        return "\n".join(str(product) for product in self.__products)

    def __repr__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"Category(name={self.name}, total_products={total_quantity})"

    def __str__(self):
        """Строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


class CategoryIterator:
    def __init__(self, category: Category):
        self._category = category
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._category._Category__products):
            product = self._category._Category__products[self._index]
            self._index += 1
            return product
        raise StopIteration
