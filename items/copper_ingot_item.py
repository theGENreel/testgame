from items.base_item import BaseItem


class CopperIngotItem(BaseItem):
    def __init__(self):
        super().__init__()
        self.set_name('Copper Ingot')
