import os
import curses
from abc import abstractmethod


class BaseOverlay:
    def __init__(self, camera, screen_multiplier: float = 0.8, pausing: bool = False):
        self.camera = camera
        self.pausing = pausing
        screen_w = os.get_terminal_size().columns
        screen_h = os.get_terminal_size().lines
        screen_w = camera.game_window.getmaxyx()[1]
        self.window = curses.newwin(int(screen_h * screen_multiplier), int(screen_w * screen_multiplier), int(screen_h * ((1 - screen_multiplier) / 2)), int(screen_w * ((1 - screen_multiplier) / 2)))

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def input(self, key):
        pass

    def string_in_mid(self, s: str):
        ans = ' ' * int((((self.window.getmaxyx()[1] - 2) - len(s)) / 2)) + s
        ans = ans + ' ' * (self.window.getmaxyx()[1] - 2 - len(ans))
        return ans
