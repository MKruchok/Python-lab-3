from enums.mechanization_tools import MechTools
from enums.customer_type import CustomerType
from game.item import Item

class MechItem(Item):
    def __init__(self, material: str, mech_item_type: MechTools, name: str, weight: int, price: int,
                rating: int, customer_type: CustomerType):
        self.material = material
        self.mech_item_type = mech_item_type
        super().__init__(name, weight, price, rating, customer_type) 

    def set_material(self, material):
        self.material = material

    def get_material(self):
        return self.material
    
    def set_mech_item_type(self, mech_item_type):
        self.mech_item_type = mech_item_type

    def get_mech_item_type(self):
        return self.mech_item_type
    