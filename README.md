# Warehouse
Warehouse is Python script for managing a warehouse product inventory,uses different methods for various operations.

## Methods used in the script 

| Methods | Description |
| ----------- | ----------- |
| **addProduct()** | Add new products to the warehouse by providing name, price, quantity, and price currency.|
| **show()** |Display a list of available products with their names, prices, and quantities. If a product is out of stock, it will be labeled as such |
| **updatePrice()**   |  Update the price of an existing product in the warehouse|
| **updateQuantity()**   |  Update the quantity of an existing product in the warehouse|
| **removeProduct()**   |  Remove a product from the warehouse|
| **product_search()**   |  Search for a specific product by name and display its details|
| **TotalValue()**  |  Calculate and display the total value of the warehouse based on the product prices and quantities|
| **price_search()**   |  Search for products by a specific price and return a list of matching products|
| **quantity_search()**  | Search for products by a specific quantity and return a list of matching products|
|**price_between()**  |  Search for products within a specific price range and return a list of matching products|
|**price_asc()**   |  Sort the products by ascending price and return a DataFrame with product names and prices|
| **price_desc()**   | Sort the products by descending price and return a DataFrame with product names and prices|
| **quantity_asc()**  |  Sort the products by ascending quantity and return a DataFrame with product names and quantities|
| **quantity_desc()**  |  Sort the products by descending quantity and return a DataFrame with product names and quantities|
| **main()**   | Provides a command-line interface to interact with the Warehouse class and choose the desired operation|

***

#### Overall, this class provides a versatile set of features for managing and analyzing the inventory of a warehouse

>purpose of this project/exercise is to practice with POP programming using classes/static methods and different methods 