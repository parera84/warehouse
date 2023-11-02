import pandas as pd

class Warehouse:
    def __init__(self):
        self.products = []


    def addProduct(self):
        while True:
            name = input("Enter the product name(or done to finish) ").lower()
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


    def product_search(self,product):
        n=input("Enter the product you want:")
        if product['name']==n:
            return(f"name{product['name']}-price{product['price']}-quantity{product['quantity']}")
        else:
            print(f"the {n} product you want do not exist in the warehouse")


    def TotalValue(self):
        total_value=0
        for product in self.products:
           total_value += product['price']*product['quantity']
        return (f"Total value of the warehouse is{total_value}")
    

    def price_search(self):
        price_list=[]
        price=float(input("Enter the price you want:"))
        for product in self.products:
            if product['price']==price:
                price_list.append(product)
        return price_list
    
    def quantity_search(self):
        quantity_list=[]
        quantity=float(input("Enter the quantity you want:"))
        for product in self.products:
            if product['quantity']==quantity:
                quantity_list.append(product)
        return quantity_list

    def price_between(self):
        min=float(input("Enter the minimum price:"))
        max=float(input("Enter the maximum price:"))
        between=[]
        for product in self.products:
            if product['price']>=min and product['price']<=max:
                between.append(product)
        return between
    
    def price_asc(self):
        # Create a copy of the original list 
        products_copy = self.products.copy()
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(products_copy) - 1):
                if products_copy[i]['price'] > products_copy[i + 1]['price']:
                    # Swap the products
                    products_copy[i], products_copy[i + 1] = products_copy[i + 1], products_copy[i]
                    swapped = True
        product_names_and_prices = [(product['name'], product['price']) for product in products_copy]
        return product_names_and_prices

    def price_desc(self):
        # Create a copy of the original list 
        products_copy = self.products.copy()
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(products_copy) - 1):
                if products_copy[i]['price'] < products_copy[i + 1]['price']:
                    # Swap the products
                    products_copy[i], products_copy[i + 1] = products_copy[i + 1], products_copy[i]
                    swapped = True
        product_names_and_prices = [(product['name'], product['price']) for product in products_copy]
        return product_names_and_prices
    
    def quantity_asc(self):
        # Create a copy of the original list 
        products_copy = self.products.copy()
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(products_copy) - 1):
                if products_copy[i]['quantity'] > products_copy[i + 1]['quantity']:
                    # Swap the products
                    products_copy[i], products_copy[i + 1] = products_copy[i + 1], products_copy[i]
                    swapped = True
        product_names_and_quantity = [(product['name'], product['quantity']) for product in products_copy]
        return product_names_and_quantity

    def quantity_desc(self):
        # Create a copy of the original list 
        products_copy = self.products.copy()
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(products_copy) - 1):
                if products_copy[i]['quantity'] < products_copy[i + 1]['quantity']:
                    # Swap the products
                    products_copy[i], products_copy[i + 1] = products_copy[i + 1], products_copy[i]
                    swapped = True
        product_names_and_quantity = [(product['name'], product['quantity']) for product in products_copy]
        return product_names_and_quantity


    @staticmethod
    def main():
        wh = Warehouse()
        while True:
            choice = int(input("Enter what you want to do:\n1. Add a new product\n2. Show the products availability\n3. Remove a product\n4. Update the price of an existing product\n5. Update the availability\n6. Search a product by name\n7. Show the total value of the warehouse\n8. Search product by price\n9. Search product by availability\n10. Search product within price range\n11. See the list of products by ascending price\n12. See the list of products by descending price\n13. See the list of products in ascending availability\n14. See the list of products in descending availability\n"))
            if choice == 1:
                wh.addProduct()
            elif choice == 2:
                wh.show()
            elif choice == 3:
                wh.removeProduct()
            elif choice == 4:
                wh.updatePrice()
            elif choice == 5:
                wh.updateQuantity()
            elif choice == 6:
                wh.product_search()
            elif choice == 7:
                wh.TotalValue()
            elif choice == 8:
                wh.price_search()
            elif choice == 9:
                wh.quantity_search()
            elif choice == 10:
                wh.price_between()
            elif choice == 11:
                wh.price_asc()
            elif choice == 12:
                wh.price_desc()
            elif choice == 13:
                wh.quantity_asc()
            elif choice == 14:
                wh.quantity_desc()
            else:
                break

if __name__ == "__main__":
    Warehouse.main()
              
            
          
                
