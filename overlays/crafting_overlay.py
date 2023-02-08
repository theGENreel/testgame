import curses
import logging

import crafts
from overlays.base_overlay import BaseOverlay
from crafts import Crafts


class CraftingOverlay(BaseOverlay):
    def __init__(self, camera):
        super().__init__(camera)
        self.category_selection = 0
        self.category_name = ''
        self.main_width = 0.7
        self.craft_selection = 0

    def draw(self):
        self.window.box('|', '-')
        self.window.move(1, 1)
        for idx, category in enumerate(Crafts.crafts):
            if idx == self.category_selection:
                self.window.addstr(category, curses.A_REVERSE)
                self.category_name = category
            else:
                self.window.addstr(category, curses.A_NORMAL)
            if idx != len(Crafts.crafts)-1:
                self.window.addstr(' ')
        self.window.addstr(2, 1, '-' * (self.window.getmaxyx()[1]-2))
        main_end = int(self.window.getmaxyx()[1] * self.main_width)
        for idx, craft in enumerate(Crafts.crafts[self.category_name]):
            self.window.move(3 + idx, 1)
            text = str(craft['out']) + (' ' * (main_end - len(str(craft['out']))))
            if idx == self.craft_selection:
                self.window.addstr(text, curses.A_REVERSE)
            elif self.camera.map.player.has_items(craft['in']):
                self.window.addstr(text, curses.A_NORMAL)
            else:
                self.window.addstr(text, curses.A_DIM)
        self.window.refresh()

    def input(self, key):
        if (key == ord('A') or key == ord('a') or key == curses.KEY_LEFT) and self.category_selection > 0:
            self.category_selection -= 1
        elif (key == ord('D') or key == ord('d') or key == curses.KEY_RIGHT) and self.category_selection < len(
                Crafts.crafts) - 1:
            self.category_selection += 1
        elif (key == ord('W') or key == ord('w') or key == curses.KEY_UP) and self.craft_selection > 0:
            self.craft_selection -= 1
        elif (key == ord('S') or key == ord('s') or key == curses.KEY_DOWN) and self.craft_selection < len(Crafts.crafts[self.category_name]) - 1:
            self.craft_selection += 1
        elif key == curses.KEY_ENTER or key == 10:
            if self.camera.map.player.has_items(Crafts.crafts[self.category_name][self.craft_selection]['in']):
                self.camera.map.player.remove_items(Crafts.crafts[self.category_name][self.craft_selection]['in'])
                self.camera.map.player.give_item(Crafts.crafts[self.category_name][self.craft_selection]['out'])
        elif key == 27:
            self.camera.overlay = None
