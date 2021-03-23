from enums.drawing_tools import DrawTools
from enums.customer_type import CustomerType
from game.item import Item


class ArtItem(Item):
    def __init__(
        self, color: str, draw_tool_type: DrawTools, name: str, weight: int,
        price: int, rating: int, customer_type: CustomerType
    ):
        self.color = color
        self.draw_tool_type = draw_tool_type
        super().__init__(name, weight, price, rating, customer_type)

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_draw_tool_type(self, draw_tool_type):
        self.draw_tool_type = draw_tool_type

    def get_draw_tool_type(self):
        return self.draw_tool_type
