class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product_data):
        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"]
        )

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        return NotImplemented


class Category:
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self._products = products if products is not None else []
        Category.product_count += len(self._products)

    @property
    def products(self):
        result = ""
        for product in self._products:
            result += str(product) + "\n"
        return result

    def add_product(self, product):
        self._products.append(product)
        Category.product_count += 1

    def __str__(self):
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
