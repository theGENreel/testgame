from fblocks.fore import FOre
from items.coal_item import CoalOreItem


class FCoalOre(FOre):
    def __init__(self):
        super().__init__(item=CoalOreItem(), count=128)
