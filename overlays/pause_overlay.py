import curses

from overlays.base_overlay import BaseOverlay


class PauseOverlay(BaseOverlay):
    def __init__(self, camera):
        super().__init__(camera, screen_multiplier=0.3)
        self.buttons = ['Continue', 'Exit game']
        self.player = camera.map.player
        self.selection = 0


    def draw(self):
        self.window.box('|', '-')

        self.window.addstr(1, 1, self.string_in_mid('Pause'))
        self.window.addstr(2, 1, '-' * (self.window.getmaxyx()[1]-2))
        for idx, button in enumerate(self.buttons):
            self.window.addstr(idx + 3, 1, self.string_in_mid(button), curses.A_REVERSE if idx == self.selection else curses.color_pair(0))
        self.window.refresh()

    def input(self, key):
        if (key == ord('W') or key == ord('w') or key == curses.KEY_UP) and self.selection > 0:
            self.selection -= 1
        elif (key == ord('S') or key == ord('s') or key == curses.KEY_DOWN) and self.selection < len(self.buttons) - 1:
            self.selection += 1
        elif key == curses.KEY_ENTER or key == 10:
            if self.selection == 0:
                self.camera.overlay = None
            elif self.selection == 1:
                self.camera.exiting = True
        elif key == 27:
            self.camera.overlay = None
