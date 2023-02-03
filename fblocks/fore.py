from fblocks.base_fblock import BaseFBlock
from items.iron_ore_item import IronOreItem


class FOre(BaseFBlock):
    def __init__(self):
        super().__init__()
        self.set_symbol('O')
        self.set_interactable(True)

    def on_interact(self, initiator):
        initiator.give_item()
