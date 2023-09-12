from items.copper_ore_item import CopperOreItem
from items.iron_ore_item import IronOreItem


class Crafts:
    crafts = {
        'Basic': [
            {'in': [(CopperOreItem(), 1)], 'out': (IronOreItem(), 2)},
            {'in': [(IronOreItem(), 2)], 'out': (CopperOreItem(), 10)}
        ]
    }