class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.inventory_slots = 10
        self.inventory = []
        self.symbol = '@'
        self.debug_str = ''

    def __str__(self):
        return self.symbol

    def give_item(self, item):
        cur = next((i for i, it in enumerate(self.inventory) if isinstance(it, type(item))), None)
        self.debug_str += str(cur) + '\n'
        if cur is not None:
            self.inventory[cur].count += item.count
        else:
            if len(self.inventory) < self.inventory_slots:
                self.inventory.append(item)
            else:
                print(f"Drop item {item}")
        # item_in_inventory = next((i for i, it in enumerate(self.inventory) if it['name'] == item['name']), None)
        # if not item_in_inventory:
        #     if len(self.inventory) < self.inventory_slots:
        #         self.inventory.append(item)
        # else:
        #     self.inventory[item_in_inventory]['count'] += item['count']

