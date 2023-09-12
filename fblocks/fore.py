from fblocks.base_fblock import BaseFBlock
from inventory.slot import Slot
from items.ore_item import OreItem


class FOre(BaseFBlock):
    def __init__(self, item: OreItem, count: int):
        super().__init__()
        self.set_symbol('O')
        self.set_interactable(True)
        self.slot = Slot(item=item, count=count, max_size=count)

    def on_interact(self, initiator):
        initiator.inventory.merge_slot(self.slot, 3)
