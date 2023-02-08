from items.ore_item import OreItem


class CopperOreItem(OreItem):
    def __init__(self, count=1):
        super().__init__(count)
        self.set_name('Copper Ore')
