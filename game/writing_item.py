from enums.writing_aids import WriteAid
from enums.customer_type import CustomerType
from game.item import Item

class WritingItem(Item):
    def __init__(self, ink_type: str, write_item_type: WriteAid, name: str, weight: int, price: int,
                rating: int, customer_type: CustomerType):
        self.ink_type = ink_type
        self.write_item_type = write_item_type
        super().__init__(name, weight, price, rating, customer_type) 

    def set_ink_type(self, ink_type):
        self.ink_type = ink_type

    def get_ink_type(self):
        return self.ink_type
    
    def set_write_item_type(self, write_item_type):
        self.write_item_type = write_item_type

    def get_write_item_type(self):
        return self.write_item_type

