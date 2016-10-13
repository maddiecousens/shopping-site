"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        return "<Customer: %s %s %s" % (self.first_name, self.last_name, self.email)

def read_customers_from_file(filepath):
    customer_data = {}

    for line in open(filepath):
        first_name, last_name, email, password = line.strip().split("|")

        customer_data[email] = Customer(first_name, last_name, email, password)

    return customer_data

customers = read_customers_from_file("customers.txt")
