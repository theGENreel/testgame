from items.base_item import BaseItem


class OreItem(BaseItem):
    def __init__(self):
        super().__init__()
        self.set_name('Ore')

    def on_interact(self, initiator):
        pass
