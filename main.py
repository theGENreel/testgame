import datetime
import os
import curses
import time

from map import Map
from camera import Camera
from player import Player


def main(screen):
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    screen.nodelay(True)
    screen.keypad(True)

    screen_w = os.get_terminal_size().columns
    screen_h = os.get_terminal_size().lines
    window_separator = int(screen_w * 0.85)
    map = Map(250, 250)
    camera = Camera(map, screen_w - (screen_w - window_separator) - 1, screen_h - 1)
    player = Player(camera)
    map.add_player(player)
    game_window = curses.newwin(screen_h, window_separator, 0, 0)
    info_window = curses.newwin(screen_h, screen_w - window_separator, 0, window_separator + 1)

    while True:
        start = datetime.datetime.now()
        game_window.clear()
        info_window.clear()
        camera.tick(screen, game_window, info_window)
        time_rest = 1 / 60 - (datetime.datetime.now() - start).seconds
        if time_rest > 0:
            time.sleep(time_rest)


if __name__ == '__main__':
    os.environ.setdefault('ESCDELAY', '0')
    curses.wrapper(main)
