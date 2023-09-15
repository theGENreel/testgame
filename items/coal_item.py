from items.ore_item import OreItem


class CoalOreItem(OreItem):
    def __init__(self):
        super().__init__()
        self.set_name('Coal Ore')
        self.burn_time = 60 * 30
