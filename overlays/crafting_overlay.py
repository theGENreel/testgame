import curses

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
        self.window.clear()
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
            text = str(craft['out'][0]) + (' ' * (main_end - len(str(craft['out'][0]))))
            if idx == self.craft_selection:
                self.window.addstr(text, curses.A_REVERSE)
            elif self.camera.map.player.inventory.has_items(craft['in'][0][0], craft['in'][0][1]): # TODO: NotDIM to multi-item crafts
                self.window.addstr(text, curses.A_NORMAL)
            else:
                self.window.addstr(text, curses.A_DIM)
        self.window.move(2, main_end)
        self.window.addstr('┬')
        for i in range(3, self.window.getmaxyx()[0] - 1):
            self.window.move(i, main_end)
            self.window.addstr('|')
        self.window.move(self.window.getmaxyx()[0] - 1, main_end)
        self.window.addstr('┴')
        self.window.move(3, main_end+1)
        self.window.addstr('Needed:')
        for idx, item in enumerate(Crafts.crafts[self.category_name][self.craft_selection]['in']):
            self.window.move(4 + idx, main_end + 1)
            count = ' ' * (self.window.getmaxyx()[1] - main_end - len(str(item[0])) - 1 - len(str(item[1])) - 1) + str(
                item[1])
            self.window.addstr(f'{item[0]}' + count)
        self.window.move(4 + idx + 2, main_end + 1)
        self.window.addstr('Output:')
        self.window.move(4 + idx + 3, main_end + 1)
        out = Crafts.crafts[self.category_name][self.craft_selection]['out']
        count = ' ' * (self.window.getmaxyx()[1] - main_end - len(str(out[0])) - 1 - len(str(out[1])) - 1) + str(out[1])
        self.window.addstr(f'{out[0]}' + count)
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
            can_craft = True
            for item, count in Crafts.crafts[self.category_name][self.craft_selection]['in']:
                if not self.camera.map.player.inventory.has_items(item, count):
                    can_craft = False
            item_out = Crafts.crafts[self.category_name][self.craft_selection]['out'][0]
            count_out = Crafts.crafts[self.category_name][self.craft_selection]['out'][1]
            if can_craft:
                for item, count in Crafts.crafts[self.category_name][self.craft_selection]['in']:
                    self.camera.map.player.inventory.remove_items(item, count)
                self.camera.map.player.inventory.add_items(item_out, count_out)
        elif key == 27:
            self.camera.overlay = None
