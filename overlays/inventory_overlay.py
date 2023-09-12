import curses

from overlays.base_overlay import BaseOverlay


class InventoryOverlay(BaseOverlay):
    def __init__(self, camera):
        super().__init__(camera)
        self.player = camera.map.player
        self.selection = 0

    def draw(self):
        self.window.box('|', '-')
        for idx, slot in enumerate(self.player.inventory.get_occupied()):
            it = str(slot.item) + (' ' * (self.window.getmaxyx()[1] - len(str(slot.item)) - len(str(slot.count)) - 4)) + str(slot.count)
            self.window.addstr(idx + 1, 2, it,
                               curses.A_REVERSE if idx == self.selection else curses.color_pair(0))
        self.window.refresh()

    def input(self, key):
        if (key == ord('W') or key == ord('w') or key == curses.KEY_UP) and self.selection > 0:
            self.selection -= 1
        elif (key == ord('S') or key == ord('s') or key == curses.KEY_DOWN) and self.selection < len(self.player.inventory.get_occupied()) - 1:
            self.selection += 1
        elif key == 27:
            self.camera.overlay = None
