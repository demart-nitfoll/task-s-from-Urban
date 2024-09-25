from pprint import pprint

class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

    def __eq__(self, other):
        return self.name == other.name and self.weight == other.weight and self.category == other.category

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        products = []
        with open(Shop.__file_name, 'r') as file:
            for line in file:
                name, weight, category = line.strip().split(', ')
                products.append(Product(name, float(weight), category))
        return products

    def add(self, *products: Product):
        existing_products = self.get_products()
        with open(Shop.__file_name, 'a') as file:
            for product in products:
                if product in existing_products:
                    print(f'Продукт {product.name} уже есть в магазине')
                else:
                    file.write(f'{product}\n')


s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products()) # не понимаю как сделать так, чтобы оно выводилось красиво через эту команду
for product in s1.get_products():
    print(product)