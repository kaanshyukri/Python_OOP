from shop.product import Product


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)
        if self.products:
            return f"{self.products}"

    def find(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        result = self.find(product_name)
        if result:
            self.products.remove(result)

    def __repr__(self):
        result = ""
        for product in self.products:
            result += f"{product.name}: {product.quantity}\n"
        return result.strip()




