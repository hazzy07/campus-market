import csv
import json

from campusmart.models import Product, Perishable, StoreError, InvalidProductError, UnknownSKUError

def write_errors(message, filename="errors.log"):
    if message:
        with open(filename, "a") as file:
                file.write(message + "\n")


def load_products(path):
     
    products = {}
    rejects = []

    with open(path, "r", newline="") as file:
          
        reader = csv.DictReader(file)

        for row in reader:

             
            try:
                price= float(row['unit_price'])
                stock= int(row['stock'])

                if stock < 0:
                    raise InvalidProductError(
                        f"Product negative stock: {stock}"
                    )

                if row['perishable'].lower() == "yes":
                    product= Perishable(
                        row['sku'],
                        row['name'],
                        row['category'],
                        price,
                        stock,
                        row['expiry'],
                    )
                else:
                    product = Product(
                        row['sku'],
                        row['name'],
                        row['category'],
                        price,
                        stock,
                    )

                products[product.sku]= product
                
            except (InvalidProductError, ValueError) as error:

                message = (
                    f"Product {row['sku']} rejected: {error}"
                )
                rejects.append(message)
                write_errors(message)
    return products, rejects


def load_sales(path, products, error_log="errors.log"):
    sales = []
    errors = []
    

    try:
        with open(path, "r", newline="") as file:
            data = json.load(file)

    except FileNotFoundError:
        message = f"Sales file not found: {path}"
        write_errors(message, error_log)
        return sales, errors
    
    except json.JSONDecodeError as error:
        message = f"Invalid sales json: {error}"
        write_errors(message, error_log)
        return sales, errors

    for sale in data:
        try:
            if sale['sku'] not in products:
                raise UnknownSKUError(
                    f"Unknown sales in {sale['txn']}, {sale['sku']}"
                )
            sales.append(sale)

        except UnknownSKUError as error:
            message = str(error)
            errors.append(message)
            write_errors(message, error_log)

    return sales, errors