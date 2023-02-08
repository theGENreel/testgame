import os
import curses
from abc import abstractmethod


class BaseOverlay:
    def __init__(self, camera):
        self.camera = camera
        screen_w = os.get_terminal_size().columns
        screen_h = os.get_terminal_size().lines
        screen_w = camera.game_window.getmaxyx()[1]
        self.window = curses.newwin(int(screen_h * 0.8), int(screen_w * 0.8), int(screen_h * 0.1), int(screen_w * 0.1))

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def input(self, key):
        pass
