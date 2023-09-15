from items.iron_ingot_item import IronIngotItem
from items.ore_item import OreItem


class IronOreItem(OreItem):
    def __init__(self):
        super().__init__()
        self.set_name('Iron Ore')
        self.smelt_time = 60 * 10
        self.smelt_to = IronIngotItem()
