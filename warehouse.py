import pandas as pd
class warehouse:
    def__init__(self):
    while true:
        name=input("Enter the product name: ").lowe()
        if name=="done":
            break
        price=float(input("Enter the price:"))
        quantity=int(input("Enter the quantity:"))
        price_currency=input("Enter the price currency:").upper()
        product={"name:",name,"price:",price,"quantity",quantity,"price_currency:",price_currency}
        self.products.append(product)
        print(product)
        print(self.products)
        return pd.DataFrame(self.products)
    
    def show(self):
        for product in self.products:
            if product["quantity"]>0:
                print(f"name{product[name]}-price{product[price]}-quantity{product[quantity]}")
            else
                print(f"{product[name]} is out of stock")

    
    