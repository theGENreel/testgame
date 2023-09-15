import curses

# from blocks.furnace import Furnace
from overlays.base_overlay import BaseOverlay
from crafts import Crafts


class FurnaceOverlay(BaseOverlay):
    def __init__(self, camera, furnace: "Furnace"):
        super().__init__(camera)
        self.furnace = furnace
        self.panel_selection = False
        self.category_name = ''
        self.main_width = 0.7
        self.inventory_selection = 0
        self.furnace_selection = 0

    def draw(self):
        self.window.box('|', '-')
        self.window.move(1, 1)
        main_end = int(self.window.getmaxyx()[1] * self.main_width)
        for idx, slot in enumerate(self.camera.map.player.inventory.get_occupied()):
            self.window.move(1 + idx, 1)
            text = str(slot.item) + (' ' * (main_end - len(str(slot.item))))
            if idx == self.inventory_selection and not self.panel_selection:
                self.window.addstr(text, curses.A_REVERSE)
            else:
                self.window.addstr(text, curses.A_NORMAL)
        self.window.move(0, main_end)
        self.window.addstr('┬')
        for i in range(1, self.window.getmaxyx()[0] - 1):
            self.window.move(i, main_end)
            self.window.addstr('|')
        self.window.move(self.window.getmaxyx()[0]-1, main_end)
        self.window.addstr('┴')
        self.window.move(1, main_end + 1)
        self.window.addstr('Input:', curses.A_REVERSE if self.furnace_selection == 0 and self.panel_selection else curses.A_NORMAL)
        self.window.move(2, main_end + 1)
        count = ' ' * (self.window.getmaxyx()[1] - main_end - len(str(self.furnace.input_slot.item)) - 1 - len(
            str(self.furnace.input_slot.count)) - 1) + str(self.furnace.input_slot.count)
        self.window.addstr(f'{self.furnace.input_slot.item}' + count, curses.A_REVERSE if self.furnace_selection == 0 and self.panel_selection else curses.A_NORMAL)
        self.window.move(4, main_end + 1)
        self.window.addstr(f'Fuel: {self.furnace.remain_burn_time}', curses.A_REVERSE if self.furnace_selection == 1 and self.panel_selection else curses.A_NORMAL)
        self.window.move(5, main_end + 1)
        count = ' ' * (self.window.getmaxyx()[1] - main_end - len(str(self.furnace.fuel_slot.item)) - 1 - len(
            str(self.furnace.fuel_slot.count)) - 1) + str(self.furnace.fuel_slot.count)
        self.window.addstr(f'{self.furnace.fuel_slot.item}' + count, curses.A_REVERSE if self.furnace_selection == 1 and self.panel_selection else curses.A_NORMAL)
        self.window.move(7, main_end + 1)
        remain_str = '' if self.furnace.input_slot.item is None else f'{self.furnace.current_progress}/{self.furnace.input_slot.item.smelt_time}' #  BUG: When remain_str disappears, symbols on overlay not cleaning
        self.window.addstr(f'Output: {remain_str}', curses.A_REVERSE if self.furnace_selection == 2 and self.panel_selection else curses.A_NORMAL)
        self.window.move(8, main_end + 1)
        count = ' ' * (self.window.getmaxyx()[1] - main_end - len(str(self.furnace.output_slot.item)) - 1 - len(
            str(self.furnace.output_slot.count)) - 1) + str(self.furnace.output_slot.count)
        self.window.addstr(f'{self.furnace.output_slot.item}' + count, curses.A_REVERSE if self.furnace_selection == 2 and self.panel_selection else curses.A_NORMAL)
        self.window.refresh()

    def input(self, key):
        if ((key == ord('A') or key == ord('a') or key == curses.KEY_LEFT) and self.panel_selection) or ((key == ord('D') or key == ord('d') or key == curses.KEY_RIGHT) and not self.panel_selection):
            self.panel_selection = not self.panel_selection
        elif key == ord('W') or key == ord('w') or key == curses.KEY_UP:
            if not self.panel_selection and self.inventory_selection > 0:
                self.inventory_selection -= 1
            elif self.panel_selection and self.furnace_selection > 0:
                self.furnace_selection -= 1
        elif key == ord('S') or key == ord('s') or key == curses.KEY_DOWN:
            if not self.panel_selection and self.inventory_selection < len(self.camera.map.player.inventory.get_occupied()) - 1:
                self.inventory_selection += 1
            elif self.panel_selection and self.furnace_selection < 2:
                self.furnace_selection += 1
        elif key == curses.KEY_ENTER or key == 10:
            if not self.panel_selection:
                ext_slot = self.camera.map.player.inventory.get_occupied()[self.inventory_selection]
                if ext_slot.item.smelt_time > 0:
                    if (ext_slot.item == self.furnace.input_slot.item and ext_slot.count > 0 and not self.furnace.input_slot.is_filled()) or self.furnace.input_slot.item is None:
                        self.furnace.input_slot.merge_slot(ext_slot, 1)
                elif ext_slot.item.burn_time > 0:
                    if (ext_slot.item == self.furnace.fuel_slot.item and ext_slot.count > 0 and not self.furnace.fuel_slot.is_filled()) or self.furnace.fuel_slot.item is None:
                        self.furnace.fuel_slot.merge_slot(ext_slot, 1)
            else:
                if self.furnace_selection == 0 and self.furnace.input_slot.count > 0:
                    self.camera.map.player.inventory.merge_slot(self.furnace.input_slot, 1)
                elif self.furnace_selection == 1 and self.furnace.fuel_slot.count > 0:
                    self.camera.map.player.inventory.merge_slot(self.furnace.fuel_slot, 1)
                elif self.furnace_selection == 2 and self.furnace.output_slot.count > 0:
                    self.camera.map.player.inventory.merge_slot(self.furnace.output_slot, 1)

        elif key == 27:
            self.camera.overlay = None
