from enums.customer_type import CustomerType

class Item:
    def __init__(self, name: str, weight: int, price: int, rating: int, customer_type: CustomerType):
        self.name = name
        self.weight = weight
        self.price = price
        self.rating = rating
        self.customer_type = customer_type


    def __repr__(self):
        return f"name: {self.name}, weight: {self.weight}, price: {self.price}, rating: {self.rating}"

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def set_rating(self, rating):
        self.price = price

    def get_rating(self):
        return self.rating
    
    def set_customer_type(self, customer_type):
        self.customer_type = customer_type

    def get_customer_type(self):
        return self.customer_type

