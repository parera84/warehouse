import pandas as pd

class Warehouse:
    def __init__(self):
        self.products = []

    def addProduct(self):
        while True:
            name = input("Enter the product name: ").lower()
            if name == "done":
                break
            price = float(input("Enter the price:"))
            quantity = int(input("Enter the quantity:"))
            price_currency = input("Enter the price currency:").upper()
            product = {"name": name, "price": price, "quantity": quantity, "price_currency": price_currency}
            self.products.append(product)
            print(product)
            print(self.products)

    def show(self):
        for product in self.products:
            if product["quantity"] > 0:
                print(f"name: {product['name']} - price: {product['price']} - quantity: {product['quantity']}")
            else:
                print(f"{product['name']} is out of stock")

    def updatePrice(self):
        name_update = input("Enter the name of the product you want to update:").lower()
        for product in self.products:
            if product["name"] == name_update:
                price_update = float(input("Enter the updated price:"))
                product["price"] = price_update
                break
        else:
            print(f"The {name_update} does not exist in the warehouse")

    def updateQuantity(self):
        name_update = input("Enter the name of the product you want to update:").lower()
        for product in self.products:
            if product["name"] == name_update:
                quantity_update = int(input("Enter the updated quantity:"))
                product["quantity"] = quantity_update
                break
        else:
            print(f"The {name_update} does not exist in the warehouse")

    def removeProduct(self):
        name_remove = input("Enter the name of the product you want to remove:").lower()
        for product in self.products:
            if name_remove == product["name"]:
                self.products.remove(product)
                print(product)
                print(self.products)
                break


    def product_search(self):
        n=input("Enter the product you want:")
        if product['name']==n:
            return(f"name{product['name']}-price{product['price']}-quantity{product['quantity']}")
        else:
            print(f"the {n} product you want do not exist in the warehouse")


    def TotalValue(self):
        total_value=[]
        sum=0
        for product in self.products:
            sum=product['price']*product['quantity']
            total_value.append(product)
        return (f"Total value of the warehouse is{total_value}")
        

