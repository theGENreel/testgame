import copy
import logging

from blocks.air import Air
from inventory.container import Container
from overlays.inventory_overlay import InventoryOverlay
from overlays.crafting_overlay import CraftingOverlay


class Player:
    def __init__(self, camera, x=0, y=0):
        self.camera = camera
        self.x = x
        self.y = y
        self.inventory = Container(10)
        self.symbol = '@'
        self.debug_str = ''
        self.selected_item = 0
        # logging.basicConfig(filename='logs/player.log', encoding='utf-8', level=logging.DEBUG)

    def __str__(self):
        return self.symbol

    # def give_item(self, item):
    #     cur = next((i for i, it in enumerate(self.inventory) if isinstance(it, type(item))), None)
    #     self.debug_str += str(cur) + '\n'
    #     if cur is not None:
    #         self.inventory[cur].count += item.count
    #     else:
    #         if len(self.inventory) < self.inventory_slots:
    #             item = copy.copy(item)
    #             self.inventory.append(item)
    #         else:
    #             print(f"Drop item {item}")
    #     # item_in_inventory = next((i for i, it in enumerate(self.inventory) if it['name'] == item['name']), None)
    #     # if not item_in_inventory:
    #     #     if len(self.inventory) < self.inventory_slots:
    #     #         self.inventory.append(item)
    #     # else:
    #     #     self.inventory[item_in_inventory]['count'] += item['count']

    # def remove_items(self, items: []):
    #     for item in items:
    #         it = next((i for i, it in enumerate(self.inventory) if type(it) == type(item)), None)
    #         if it is not None:
    #             self.inventory[it].count -= item.count
    #             if self.inventory[it].count <= 0:
    #                 self.inventory.pop(it)

    # def has_items(self, items: []):
    #     for item in items:
    #         it = next((i for i, it in enumerate(self.inventory) if type(it) == type(item)), None)
    #         if it is None:
    #             return False
    #         elif self.inventory[it].count < item.count:
    #             return False
    #     return True

    def input(self, key):
        # Player Movement
        if key == ord('W') or key == ord('S') or key == ord('A') or key == ord('D') or key == ord('w') or key == ord(
                's') or key == ord('a') or key == ord('d'):
            if key == ord('W') or key == ord('w'):
                if self.y > 0:
                    if not self.camera.map.body_layer[self.x][self.y - 1].opaque:
                        self.camera.map.body_layer[self.y - 1][self.x] = self
                        self.camera.map.body_layer[self.y][self.x] = Air()
                        self.y = self.y - 1
            elif key == ord('S') or key == ord('s'):
                if self.y < self.camera.map.height - 1:
                    if not self.camera.map.body_layer[self.x][self.y + 1].opaque:
                        self.camera.map.body_layer[self.y + 1][self.x] = self
                        self.camera.map.body_layer[self.y][self.x] = Air()
                        self.y = self.y + 1
            elif key == ord('A') or key == ord('a'):
                if self.x > 0:
                    if not self.camera.map.body_layer[self.x - 1][self.y].opaque:
                        self.camera.map.body_layer[self.y][self.x - 1] = self
                        self.camera.map.body_layer[self.y][self.x] = Air()
                        self.x = self.x - 1
            elif key == ord('D') or key == ord('d'):
                if self.x < self.camera.map.width - 1:
                    if not self.camera.map.body_layer[self.x + 1][self.y].opaque:
                        self.camera.map.body_layer[self.y][self.x + 1] = self
                        self.camera.map.body_layer[self.y][self.x] = Air()
                        self.x = self.x + 1
        # Interacting
        elif key == ord('E') or key == ord('e'):
            self.debug_str += 'Interact pressed\n'
            if self.camera.map.floor_layer[self.y][self.x].interactable:
                self.debug_str += 'Interact\n'
                self.camera.map.floor_layer[self.y][self.x].on_interact(self)
        elif key == ord('1') or key == ord('2') or key == ord('3') or key == ord('4') or key == ord('5') or key == ord(
            '6') or key == ord('7') or key == ord('8') or key == ord('9') or key == ord('0'):
            c = chr(key)
            new_index = 9 if c == '0' else str(int(c) - 1)
            if int(new_index) < len(self.inventory.slots):
                self.selected_item = int(new_index)
        elif key == ord('I') or key == ord('i'):
            self.camera.overlay = InventoryOverlay(self.camera)
        elif key == ord('C') or key == ord('c'):
            self.camera.overlay = CraftingOverlay(self.camera)

