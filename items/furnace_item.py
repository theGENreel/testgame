from blocks.furnace import Furnace
from items.base_item import BaseItem


class FurnaceItem(BaseItem):
    def __init__(self):
        super().__init__()
        self.set_name('Furnace')
        self.set_placeable(True, Furnace)

    def on_interact(self, initiator):
        pass
