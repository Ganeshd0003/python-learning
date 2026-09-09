# Given a dictionary of products and their prices, find the product with the highest price.

products = {"laptop": 10,"bag": 2,"TV":15}

highest = max(products, key=products.get)
print(highest, products[highest])