from fblocks.fore import FOre
from items.copper_ore_item import CopperOreItem


class FCopperOre(FOre):
    def __init__(self):
        super().__init__()

    def on_interact(self, initiator):
        initiator.give_item(CopperOreItem())
