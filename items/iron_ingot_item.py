from items.base_item import BaseItem


class IronIngotItem(BaseItem):
    def __init__(self):
        super().__init__()
        self.set_name('Iron Ingot')
