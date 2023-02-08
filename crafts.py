from items.copper_ore_item import CopperOreItem
from items.iron_ore_item import IronOreItem


class Crafts:
    crafts = {
        'Basic': [
            {'in': [CopperOreItem(count=10)], 'out': IronOreItem(count=2)},
            {'in': [IronOreItem(count=2)], 'out': CopperOreItem(count=10)}
        ]
    }