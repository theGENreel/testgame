from items.ore_item import OreItem


class IronOreItem(OreItem):
    def __init__(self):
        super().__init__()
        self.set_name('Iron Ore')
