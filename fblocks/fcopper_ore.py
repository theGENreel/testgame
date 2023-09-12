from fblocks.fore import FOre
from items.copper_ore_item import CopperOreItem


class FCopperOre(FOre):
    def __init__(self):
        super().__init__(item=CopperOreItem(), count=150)
