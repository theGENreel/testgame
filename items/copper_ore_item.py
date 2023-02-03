from items.ore_item import OreItem


class CopperOreItem(OreItem):
    def __init__(self):
        super().__init__()
        self.set_name('Copper Ore')
