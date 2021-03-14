from enums.sort_order import SortOrder
from enums.customer_type import CustomerType


class StoreItemManager:

    def __init__(self, items: []):
        self.items = items

    def sort_by_rating(self, items: [] = None, order: SortOrder = 0):
        return sorted(items if items else self.items, key = lambda x: x.get_rating(),reverse = order.value if order else False)

    def sort_by_price(self, items: [] = None, order: SortOrder = 0):
        return sorted(items if items else self.items, key = lambda x: x.get_price(),reverse = order.value if order else False)

    def search_by_type(self, customer_type: CustomerType):
        return f"Found items for {customer_type.name}: {[Item for Item in self.items if Item.get_customer_type() == customer_type]}"
