from blocks.pipe import Pipe
from blocks.stone import Stone
from items.base_item import BaseItem


class PipeItem(BaseItem):
    def __init__(self):
        super().__init__()
        self.set_name('Pipe')
        self.set_placeable(True, Pipe)

    def on_interact(self, initiator):
        pass
