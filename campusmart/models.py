from datetime import date

class StoreError(Exception):
    """Error for the store"""

class InvalidProductError(StoreError):
    """Invalid Product"""

class UnknownSKUError(StoreError):
    """Unknow sku"""


class Product:
    count = 0

    def __init__(self, sku, name, category, unit_price, stock):
        self.sku = sku
        self.name = name
        self.category = category
        self.unit_price = float(unit_price)
        self.stock = int(stock)
        Product.count += 1

    def __repr__(self):
        return (
            f"Product({self.sku}, {self.name}, "
            f"{self.category}, {self.unit_price}, {self.stock})"
        )
    

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented

        return self.sku == other.sku

    def __hash__(self):
        return hash(self.sku)

    @property
    def total_value(self):
        return self.unit_price * self.stock

    def status(self):
        return "LOW" if self.stock < 10 else "OK"


class Perishable(Product):

    def __init__(self, sku, name, category, unit_price, stock, expiry):
        super().__init__(sku, name, category, unit_price, stock)
        self.expiry = date.fromisoformat(expiry)

    def status(self):
        if self.expiry < date.today():
            return "EXPIRED"
        return super().status()

 
        