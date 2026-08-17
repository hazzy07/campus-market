from campusmart.loaders import load_products, load_sales

products, rejects = load_products("products.csv")

sales, errors = load_sales('sales.json', products)


print("Products:")
print(products)

print("Rejected Products:")
print(rejects)

print("Sales Products:")
print(sales)

print("Error Sales Products")
print(errors)