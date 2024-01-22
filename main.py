import datetime
import os
import curses
import threading
import time
import sys

from map import Map
from camera import Camera
from entities.player import EntityPlayer


def tick_generator(camera: Camera, map: Map, player: EntityPlayer):
    tps = 20
    while not camera.exiting:
        start_frame_time = datetime.datetime.now()
        if camera.overlay is None or (camera.overlay is not None and not camera.overlay.pausing):
            player.tick()
            for block in map.ticking_blocks:
                if block.is_ticking():
                    block.tick()
            for mob in map.ticking_mobs:
                mob.tick()
        frame_time = datetime.datetime.now() - start_frame_time
        time_to_sleep = (((1 / float(tps)) * 1000000) - frame_time.microseconds) / 1000000.0
        with open('tps', 'w') as file:
            file.write(str(1 / ((frame_time.microseconds + (time_to_sleep * 1000000.0)) / 1000000.0)))
        if time_to_sleep > 0:
            time.sleep(time_to_sleep)


def game(map: Map, camera: Camera, player: EntityPlayer, game_window, info_window):
    threading.Thread(target=tick_generator, args=[camera, map, player]).start()
    while not camera.exiting:
        start = datetime.datetime.now()
        game_window.clear()
        info_window.clear()
        camera.tick()
        time_rest = 1 / 60 - (datetime.datetime.now() - start).seconds
        if time_rest > 0:
            time.sleep(time_rest)
    sys.exit(0)

def new_game(screen):
    screen_w = os.get_terminal_size().columns
    screen_h = os.get_terminal_size().lines
    window_separator = int(screen_w * 0.85)
    map = Map(250, 250)
    game_window = curses.newwin(screen_h, window_separator, 0, 0)
    info_window = curses.newwin(screen_h, screen_w - window_separator, 0, window_separator + 1)
    camera = Camera(screen, map, screen_w - (screen_w - window_separator) - 1, screen_h - 1, game_window, info_window)
    player = EntityPlayer(camera)
    map.add_player(player)
    game(map, camera, player, game_window, info_window)


def main_menu(screen):
    buttons = ['New Game', 'Exit']
    selection = 0
    while True:
        for idx, button in enumerate(buttons):
            screen.addstr(1 + idx, 1, button, curses.A_REVERSE if idx == selection else curses.A_NORMAL)

        key = screen.getch()
        if key == ord('W') or key == ord('w') or key == curses.KEY_UP and selection > 0:
            selection -= 1
        elif key == ord('S') or key == ord('s') or key == curses.KEY_DOWN and selection < len(buttons)-1:
            selection += 1
        elif key == curses.KEY_ENTER or key == 10:
            if selection == 0:
                new_game(screen)
            elif selection == 1:
                sys.exit(0)
        screen.refresh()


def main(screen):
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    screen.nodelay(True)
    screen.keypad(True)
    main_menu(screen)


if __name__ == '__main__':
    os.environ.setdefault('ESCDELAY', '0')
    curses.wrapper(main)
