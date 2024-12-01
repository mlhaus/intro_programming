# Page 377
from click import password_option


class Product:
    # Attributes
    name:str
    price:float

    # Page 381, constructor
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Page 377, getters
    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    # setters
    def setName(self, name):
        self.name = name

    def setPrice(self, price):
        # page 249
        if(price < 0):
            raise ValueError("Price cannot be negative")
        self.price = price

def main():
    # Instantiate Product objects
    product1 = Product("Phone", 500)
    product2 = Product("Charger", 4.99)
    product3 = Product("Pencil", 1.99)
    product4 = Product("Tablet", 800)
    product5 = Product("Camera", 250)
    product6 = Product("Mouse", 25)
    try:
        product6.setPrice(50)
    except ValueError:
        pass
    products = []
    products.append(product1)
    products.append(product2)
    products.append(product3)
    products.append(product4)
    products.append(product5)
    products.append(product6)
    for product in products:
        print(f"{product.getName()} costs {product.getPrice()}")

if __name__ == "__main__":
    main()