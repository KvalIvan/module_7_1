from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self, __file_name='products.txt'):
        self.__file_name = __file_name

    def get_product(self):
        file = open(self.__file_name, 'r')
        pprint(file.read())
        file.close()

    def add(self, *products: Product):
        for product in products:
            file = open(self.__file_name, 'r')
            if str(product) not in file.read():
                file.close()
                file = open(self.__file_name, 'a')
                file.write(f'{product}\n')
                file.close()
            else:
                print(f'Продукт {product} уже есть в магазине')



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)  # __str__
s1.add(p1, p2, p3)
print(s1.get_product())
