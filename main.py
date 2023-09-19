import datetime
import os
import curses
import time

from map import Map
from camera import Camera
from entities.player import EntityPlayer


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
    game_window = curses.newwin(screen_h, window_separator, 0, 0)
    info_window = curses.newwin(screen_h, screen_w - window_separator, 0, window_separator + 1)
    camera = Camera(screen, map, screen_w - (screen_w - window_separator) - 1, screen_h - 1, game_window, info_window)
    player = EntityPlayer(camera)
    map.add_player(player)

    while not camera.exiting:
        start = datetime.datetime.now()
        game_window.clear()
        info_window.clear()
        camera.tick()
        if camera.overlay is None or (camera.overlay is not None and not camera.overlay.pausing):
            player.tick()
            for block in map.ticking_blocks:
                if block.is_ticking():
                    block.tick()
            for mob in map.ticking_mobs:
                mob.tick()

        time_rest = 1 / 60 - (datetime.datetime.now() - start).seconds
        if time_rest > 0:
            time.sleep(time_rest)


if __name__ == '__main__':
    os.environ.setdefault('ESCDELAY', '0')
    curses.wrapper(main)
