from items.copper_ingot_item import CopperIngotItem
from items.ore_item import OreItem


class CopperOreItem(OreItem):
    def __init__(self):
        super().__init__()
        self.set_name('Copper Ore')
        self.smelt_time = 60 * 6
        self.smelt_to = CopperIngotItem()
