from items.base_item import BaseItem


class OreItem(BaseItem):
    def __init__(self, count=1):
        super().__init__(count)
        self.set_name('Ore')

    def on_interact(self, initiator):
        pass
