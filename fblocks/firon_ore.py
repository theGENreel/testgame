from fblocks.fore import FOre
from items.iron_ore_item import IronOreItem


class FIronOre(FOre):
    def __init__(self):
        super().__init__(item=IronOreItem(), count=128)
