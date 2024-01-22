import curses
from typing import Type, Union

from blocks.air import Air
from entities.base_entity import BaseEntity
from inventory.container import Container
from inventory.slot import Slot
from items.furnace_item import FurnaceItem
from overlays.base_overlay import BaseOverlay
from overlays.inventory_overlay import InventoryOverlay
from overlays.crafting_overlay import CraftingOverlay
from overlays.pause_overlay import PauseOverlay


class EntityPlayer(BaseEntity):
    def __init__(self, camera, x=0, y=0):
        super().__init__(camera.map, '@', 0, 0)
        self.camera = camera
        self.inventory = Container(10)
        self.inventory.slots[0].item = FurnaceItem()
        self.inventory.slots[0].count = 1
        self.debug_str = ''
        self.selected_item = 0
        self.show_side = False
        self.show_side_counter = 0
        self.speed = 10

    def set_overlay(self, overlay: Union[Type[BaseOverlay], None]):
        self.camera.overlay = overlay

    def tick(self):
        super().tick()
        if self.show_side_counter < 30:
            self.show_side_counter += 1
        else:
            self.show_side_counter = 0
            self.show_side = not self.show_side

        if self.show_side:
            if self.side == 'l':
                self.symbol = '<'
            elif self.side == 'r':
                self.symbol = '>'
            elif self.side == 'u':
                self.symbol = '^'
            elif self.side == 'd':
                self.symbol = 'v'
        else:
            self.symbol = '@'

    def interact(self):
        y = self.x - 1 if self.side == 'l' else self.x + 1 if self.side == 'r' else self.x
        x = self.y - 1 if self.side == 'u' else self.y + 1 if self.side == 'd' else self.y
        if x >= 0 and y >= 0 and self.camera.map.body_layer[x][y].interactable:
            self.camera.map.body_layer[x][y].on_interact(self)
        elif self.camera.map.body_layer[self.y][self.x]:
            if self.camera.map.floor_layer[self.y][self.x].interactable:
                self.debug_str += 'Interact\n'
                self.camera.map.floor_layer[self.y][self.x].on_interact(self)

    def place_block(self, slot: Slot):
        if slot.item is not None:
            if slot.count > 0 and slot.item.placeable:
                y = self.x-1 if self.side == 'l' else self.x+1 if self.side == 'r' else self.x
                x = self.y-1 if self.side == 'u' else self.y+1 if self.side == 'd' else self.y
                if x > 0 and y > 0 and isinstance(self.camera.map.body_layer[x][y], Air):
                    self.camera.map.body_layer[x][y] = slot.item.block()
                    slot.count -= 1
                    if slot.count == 0:
                        slot.item = None
                    side_blocks = {
                        'l': self.camera.map.body_layer[x][y-1] if y-1 >= 0 else None,
                        'r': self.camera.map.body_layer[x][y+1] if y+1 <= self.camera.map.width-1 else None,
                        'u': self.camera.map.body_layer[x-1][y] if x-1 >= 0 else None,
                        'd': self.camera.map.body_layer[x+1][y] if x+1 <= self.camera.map.height-1 else None
                    }
                    if isinstance(side_blocks['l'], EntityPlayer):
                        side_blocks['l'] = self.inside_block
                    if isinstance(side_blocks['r'], EntityPlayer):
                        side_blocks['r'] = self.inside_block
                    if isinstance(side_blocks['u'], EntityPlayer):
                        side_blocks['u'] = self.inside_block
                    if isinstance(side_blocks['d'], EntityPlayer):
                        side_blocks['d'] = self.inside_block
                    self.camera.map.body_layer[x][y].on_place(side_blocks, self)
                    self.camera.map.ticking_blocks.append(self.camera.map.body_layer[x][y])

    def input(self, key):
        # Player Movement
        if key == ord('W') or key == ord('w') or key == curses.KEY_UP:
            self.move_up()
        elif key == ord('S') or key == ord('s') or key == curses.KEY_DOWN:
            self.move_down()
        elif key == ord('A') or key == ord('a') or key == curses.KEY_LEFT:
            self.move_left()
        elif key == ord('D') or key == ord('d') or key == curses.KEY_RIGHT:
            self.move_right()
        # Interacting
        elif key == ord('E') or key == ord('e'):
            self.debug_str += 'Interact pressed\n'
            self.interact()
        elif key == ord('1') or key == ord('2') or key == ord('3') or key == ord('4') or key == ord('5') or key == ord(
            '6') or key == ord('7') or key == ord('8') or key == ord('9') or key == ord('0'):
            c = chr(key)
            new_index = 9 if c == '0' else str(int(c) - 1)
            if int(new_index) < len(self.inventory.slots):
                self.selected_item = int(new_index)
        elif key == ord('I') or key == ord('i'):
            self.set_overlay(InventoryOverlay(self.camera))
        elif key == ord('C') or key == ord('c'):
            self.set_overlay(CraftingOverlay(self.camera))
        elif key == ord('P') or key == ord('p'):
            self.place_block(self.inventory.slots[self.selected_item])
        elif key == 27:
            self.set_overlay(PauseOverlay(self.camera))

