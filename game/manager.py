from pprint import pprint
import unittest
from enums.customer_type import CustomerType
from enums.sort_order import SortOrder
from enums.writing_aids import WriteAid
from enums.drawing_tools import DrawTools
from enums.mechanization_tools import MechTools
from game.mech_item import MechItem
from game.writing_item import WritingItem
from game.art_item import ArtItem
from game.store_item_manager import StoreItemManager
from game.test import TestManager


if __name__ == '__main__':
    pen = WritingItem("standard", WriteAid.PEN, "Vector", 20, 10, 5, CustomerType.HIGHSCHOOL)
    pencil = WritingItem("none", WriteAid.PENCIL, "MARK", 15, 5, 4, CustomerType.HIGHSCHOOL)
    colorpencil = ArtItem("red", DrawTools.COLORPENCIL, "Dream-pencil", 15, 7, 4, CustomerType.JUNIOR)
    brush = ArtItem("none", DrawTools.BRUSH, "Cloud-brush", 50, 20, 5, CustomerType.JUNIOR)
    stapler = MechItem("steel", MechTools.STAPLER, "Gold", 300, 100, 5, CustomerType.STUDENT)
    holepuncher = MechItem("plastic", MechTools.HOLEPUNCH, "Holer", 250, 75, 3, CustomerType.STUDENT)
    store_item_manager = StoreItemManager([pen, pencil, colorpencil, brush, stapler, holepuncher])

    print("Items:")
    pprint(store_item_manager.items)
    print("Sort by price:")
    pprint(store_item_manager.sort_by_price())
    print("Sort by rating:")
    pprint(store_item_manager.sort_by_rating([colorpencil, brush, holepuncher], SortOrder.DESC))
    print("Search for junior:")
    pprint(store_item_manager.search_by_type(CustomerType.JUNIOR))
    unittest.main()
