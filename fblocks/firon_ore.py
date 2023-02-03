from fblocks.fore import FOre
from items.iron_ore_item import IronOreItem


class FIronOre(FOre):
    def __init__(self):
        super().__init__()

    def on_interact(self, initiator):
        initiator.give_item(IronOreItem())
