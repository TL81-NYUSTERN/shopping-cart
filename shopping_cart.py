# shopping_cart.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

# TODO: write some Python code here to produce the desired output

products_id = [x['id'] for x in products] # building list of all the IDs in the entire product list and also converting to string datatype 

print(products_id)

order_id = []

while True:

    x = input(f'Please input ID number of item. If the order is complete, input "DONE". ')

    if x == "DONE": 
        break    

    try: # check to make sure input is a number
        x = int(x)
    except ValueError:
        print(f'Invalid entry. Please try again.')
        continue

    if int(x) not in products_id: # check to make sure item ID is in the product list
        x = print(f'Item ID not found.')

    else:
        order_id.append(int(x))


from datetime import datetime
current_datetime = datetime.now().strftime("%m/%d/%Y %I:%M %p") # getting the current date and time for the receipt


print(f"""---------------------------------
TRAITOR JOES
WWW.TRAITORJOES.COM
---------------------------------
CHECKOUT AT: {current_datetime}
---------------------------------""")

product_ids = [1, 8, 6, 16, 6] # temporary list of valid ids for testing purposes

print("SHOPPING CART ITEMS:", order_id)

def name_lookup(i):
    product_name = [x['name'] for x in products if x['id'] == i] # list comprehension to get the name based on ID
    return product_name[0]

def price_lookup(i):
    product_price = [float(x['price']) for x in products if x['id'] == i] # list comprehension to get the price based on ID and also converting datatype to float
    return product_price[0]

order_total = 0

for y in order_id: # looping through each product in the list
    print(f" -  {name_lookup(y)} ({to_usd(price_lookup(y))})") # printing name and price for product
    order_total = order_total + price_lookup(y) # adding price of product to running total

#print(to_usd(order_total))

tax_rate = 8.75 / 100 # tax rate set to NYC sales tax rate of 8.75%

tax_total = order_total * tax_rate

total_with_tax = order_total + tax_total # sum of order subtotal and tax

print(f"""---------------------------------
SUBTOTAL: {to_usd(order_total)}
TAX: {to_usd(tax_total)}
TOTAL: {to_usd(total_with_tax)}
---------------------------------
THANK YOU FOR SHOPPING AT TRAITOR JOES!""")






