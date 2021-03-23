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


class TestManager(unittest.TestCase):
    def test_all(self):
        pen = WritingItem("standard", WriteAid.PEN, "Vector", 20, 10, 5, CustomerType.HIGHSCHOOL)
        pencil = WritingItem("none", WriteAid.PENCIL, "MARK", 15, 5, 4, CustomerType.HIGHSCHOOL)
        colorpencil = ArtItem("red", DrawTools.COLORPENCIL, "Dream-pencil", 15, 7, 4, CustomerType.JUNIOR)
        brush = ArtItem("none", DrawTools.BRUSH, "Cloud-brush", 50, 20, 5, CustomerType.JUNIOR)
        stapler = MechItem("steel", MechTools.STAPLER, "Gold", 300, 100, 5, CustomerType.STUDENT)
        holepuncher = MechItem("plastic", MechTools.HOLEPUNCH, "Holer", 250, 75, 3, CustomerType.STUDENT)
        test_manager = StoreItemManager([pen, pencil, colorpencil, brush, stapler, holepuncher])

        self.assertEqual(
            sorted(test_manager.items, key=lambda x: x.get_price(), reverse=False),
            StoreItemManager.sort_by_price(test_manager.items, test_manager.items, SortOrder.ASC)
            )

        self.assertEqual(
            sorted(test_manager.items, key=lambda x: x.get_price(), reverse=True),
            StoreItemManager.sort_by_price(test_manager.items, test_manager.items, SortOrder.DESC)
            )

        self.assertEqual(
            sorted(test_manager.items, key=lambda x: x.get_rating(), reverse=False),
            StoreItemManager.sort_by_rating(test_manager.items, test_manager.items, SortOrder.ASC)
            )

        self.assertEqual(
            sorted(test_manager.items, key=lambda x: x.get_rating(), reverse=True),
            StoreItemManager.sort_by_rating(test_manager.items, test_manager.items, SortOrder.DESC)
            )

        self.assertEqual(
            f"Found items for JUNIOR: {[Item for Item in test_manager.items if Item.get_customer_type() == CustomerType.JUNIOR]}",
            StoreItemManager.search_by_type(test_manager, CustomerType.JUNIOR)
            )

        self.assertEqual(
            f"Found items for STUDENT: {[Item for Item in test_manager.items if Item.get_customer_type() == CustomerType.STUDENT]}",
            StoreItemManager.search_by_type(test_manager, CustomerType.STUDENT)
            )

        self.assertEqual(
            f"Found items for HIGHSCHOOL: {[Item for Item in test_manager.items if Item.get_customer_type() == CustomerType.HIGHSCHOOL]}",
            StoreItemManager.search_by_type(test_manager, CustomerType.HIGHSCHOOL)
            )
