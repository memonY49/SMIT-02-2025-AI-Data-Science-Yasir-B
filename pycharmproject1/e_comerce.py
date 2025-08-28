# Realistic E-Commerce Order System with CSV, Logging, and Time
# You will build a mini E-commerce order management system in Python. This project will help you practice:
#
# OOP concepts: Instance Methods, Class Methods, Static Methods, Decorators
# File handling: CSV (for products) + TXT (for logs)
# Timestamps in logs using Python’s datetime module
# 1. Prepare a Product CSV File
# Create a file named products.csv in the same folder as your Python script.
# Add some products like this:
#
# Example product.csv,
#
# id,name,price
#
# 1,Laptop,1200
#
# 2,Phone,800
#
# 3,Headphones,150
#
# 4,Mouse,40
#
# 5,Keyboard,60
#
#
#
# 2. Define the Order Class
# Inside your Python program, create an Order class.
#
#
#
# a. Instance Methods
# add_item_by_id(product_id, quantity)
# Reads from products.csv.
# Finds the product with the given id.
# Adds the product (with its price × quantity) to the order.
# Logs the action into log.txt with the current time.
# Example log:
# 					[2025-08-19 14:30:12] Added item: Laptop (x2) - Total: 2400
#
# calculate_total()
# Calculates the order’s total cost.
# Applies any global discount (if set).
# Logs the calculation with time into log.txt.
# Example log:
# 					[2025-08-19 14:32:05] Calculated total with discount: 2700
#
# b. Class Method
# set_discount(cls, discount_rate)
# Sets a global discount percentage for all orders.
# Logs with time:
# 					[2025-08-19 14:35:10] Discount set to 10%
#
#
#
# c. Static Method
# is_valid_product_id(product_id)
# Checks if the given product ID exists in products.csv.
# If invalid, logs with time:
# 					[2025-08-19 14:36:20] Invalid product ID attempt: 99
#
# d. Decorator (inside class)
# @log_action
# A decorator that automatically logs "Executed <method_name>" with timestamp into log.txt whenever the method is called.
# Example:
# 					[2025-08-19 14:40:45] Executed add_item_by_id
#
#
#
# 3. Testing the System
# Do the following in your main code:
#
# Create an Order object.
# Add items using their ID and a quantity (example: Laptop × 2, Mouse × 3).
# Try adding an invalid product ID.
# Apply a discount (e.g., 10%) using the class method.
# Calculate the total.
# Open log.txt → confirm that every action has a timestamp.

from datetime import datetime as dt

class order:
    orders = []

    def logger(func):
        def wrapper(*args, **kwargs):
            with open("log.txt", 'a') as log_file:
                running_log = f"{dt.now()} '{func.__name__}' is called.....\n"
                log_file.write(running_log)
                result = func(*args, **kwargs)
            return result

        return wrapper

    @logger
    def add_item_by_id(self,product_id, quantity):
        products = []
        with open('product.csv', 'r') as file:
            products = [line.strip().split(',') for line in file.readlines()]
            products.pop(0)
        for product in products:
            if product[0] == product_id:
                self.orders.append({"product_id": product_id,
                                    'quantity': quantity,
                                    "total": product[2]*quantity})






# pip install notebook
# python -m pip install notebook
# py -m pip install notebook










