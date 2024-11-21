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

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать продукты разных типов.")
        total_quantity = self.quantity + other.quantity
        return Product(self.name, self.description, self.price, total_quantity)


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __repr__(self):
        return (f"Smartphone({super().__repr__()}, efficiency={self.efficiency}, "
                f"model={self.model}, memory={self.memory}, color={self.color})")

    @classmethod
    def new_product(cls, product_info):
        """Создание нового смартфона."""
        return cls(
            product_info["name"],
            product_info["description"],
            product_info["price"],
            product_info["quantity"],
            product_info["efficiency"],
            product_info["model"],
            product_info["memory"],
            product_info["color"],
        )


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __repr__(self):
        return (f"LawnGrass({super().__repr__()}, country={self.country}, "
                f"germination_period={self.germination_period}, color={self.color})")

    @classmethod
    def new_product(cls, product_info):
        """Создание новой травы газонной."""
        return cls(
            product_info["name"],
            product_info["description"],
            product_info["price"],
            product_info["quantity"],
            product_info["country"],
            product_info["germination_period"],
            product_info["color"],
        )


class Category:
    total_categories = 0
    product_count = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__products = []
        # Увеличиваем количество категорий
        Category.total_categories += 1

    def add_product(self, product: Product):
        if not isinstance(product, (Smartphone, LawnGrass, Product)):
            raise TypeError("Можно добавлять только продукты или их наследники.")
        self.__products.append(product)
        Category.product_count += 1

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
