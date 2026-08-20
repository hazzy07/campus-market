# CampusMart

CampusMart is a Python inventory and sales data handling project.

Currently, the project focuses on **product models and loading/validation of CSV and JSON data** using only the Python standard library.

## Current Project Structure

```text
CampusMart/
│
├── campusmart/
│   ├── __init__.py
│   ├── models.py
│   └── loaders.py
│
├── products.csv
├── sales.json
└── README.md
```

## Current Features

### Models

The `models.py` module contains:

* `StoreError`
* `InvalidProductError`
* `UnknownSKUError`
* `Product`
* `Perishable`

The `Product` class currently supports:

* SKU
* Name
* Category
* Unit price
* Stock
* `__repr__`
* `__eq__` comparison by SKU
* `__hash__`
* `total_value` property
* `status()` method
* Class-level object counter using `Product.count`

The `Perishable` class extends `Product` and adds an expiry date.

Its `status()` method can return:

* `OK`
* `LOW`
* `EXPIRED`

## Data Loading

The `loaders.py` module currently handles:

### Products

Products are loaded from `products.csv`.

The loader:

* Reads CSV data using `csv.DictReader`
* Converts price to `float`
* Converts stock to `int`
* Rejects negative stock
* Rejects invalid numeric prices
* Creates `Product` or `Perishable` objects
* Returns valid products as a dictionary keyed by SKU
* Stores rejected product messages in a rejects list
* Writes errors to `errors.log`

### Sales

Sales are loaded from `sales.json`.

The loader currently handles:

* JSON loading
* Missing sales files
* Invalid JSON
* Unknown SKUs
* Error logging

Sales containing an unknown SKU are skipped instead of crashing the program.

## Input Files

### products.csv

The current sample data contains valid and intentionally invalid product records.

Invalid examples include:

```text
B201 → negative stock
C300 → invalid price "abc"
```

### sales.json

The current sample sales contain:

```text
T1 → A100
T2 → B200
T3 → Z999
```

`Z999` does not exist in the product catalogue, so it is handled as an `UnknownSKUError` and logged.

## Error Log

Errors are written to:

```text
errors.log
```

Example errors:

```text
Product B201 rejected: negative stock: -5
Product C300 rejected: could not convert string to float: 'abc'
Unknown sales in T3, Z999
```

## Technologies

* Python
* CSV
* JSON
* Object-Oriented Programming
* Exception Handling
* Python Standard Library

## Status

This project is currently under development.

The current stage covers:

* Product models
* Custom exceptions
* CSV product loading
* JSON sales loading
* Data validation
* Error handling and logging

## Testing

The current implementation can be tested using `main.py`.

Run:

```bash
python3 main.py