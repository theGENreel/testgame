from blocks.air import Air


class Camera:
    def __init__(self, screen, map, width, height, game_window, info_window):
        self.screen = screen
        self.width = width
        self.height = height
        self.map = map
        self.game_window = game_window
        self.info_window = info_window
        self.x = 0
        self.y = 0
        self.debug_str = ''
        self.overlay = None

    def tick(self):
        key = self.screen.getch()
        if not self.overlay:
            self.draw(self.game_window)
            self.draw_info(self.info_window)
            self.map.player.input(key)
        else:
            self.overlay.draw()
            self.draw_info(self.info_window)
            self.overlay.input(key)

    # Draw gameplay screen
    def draw(self, screen):
        self.update()
        for line in range(self.y, self.height + self.y):
            for cell in range(self.x, self.width + self.x):
                # If body have not a block on body layer, then draw cell from floor layer.
                if isinstance(self.map.body_layer[line][cell], Air):
                    pass
                    screen.addstr(str(self.map.floor_layer[line][cell]))
                else:
                    screen.addstr(str(self.map.body_layer[line][cell]))
            screen.addstr('\n')

        screen.refresh()

    # Draw info screen
    def draw_info(self, screen):
        screen.addstr(0, 0, f'{self.map.player.x}:{self.map.player.y}  {self.map.player.side}\n')
        screen.addstr('Inventory:\n')
        for idx, slot in enumerate(self.map.player.inventory.slots):
            if idx == self.map.player.selected_item:
                screen.addstr('*')
            screen.addstr(f'{str(slot.item)}: {slot.count}\n')

        # screen.addstr('Map debug:\n')
        # for line in self.map.debug_str.splitlines()[-3:]:
        #     screen.addstr(f'{line}\n')
        # screen.addstr('Player debug:\n')
        # for line in self.map.player.debug_str.splitlines()[-3:]:
        #     screen.addstr(f'{line}\n')

        screen.refresh()

    # Make camera follow player
    def update(self):
        if self.map.player.x - self.x < self.width * 0.2 and self.x > 0:
            self.x -= 1
        if self.map.player.x - self.x > self.width * 0.8 and self.x + self.width < self.map.width:
            self.x += 1
        if self.map.player.y - self.y < self.height * 0.2 and self.y > 0:
            self.y -= 1
        if self.map.player.y - self.y > self.height * 0.8 and self.y + self.height < self.map.height:
            self.y += 1

