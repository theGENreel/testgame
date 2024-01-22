from blocks.air import Air


class BaseEntity:
    def __init__(self, map: "Map", symbol: str, x: int, y: int):
        self.map = map
        self.symbol = symbol
        self.x = x
        self.y = y
        self.side = 'r'
        self.inside_block = Air()
        self.tick_counter = 0
        self.speed = 7

    def __str__(self):
        return self.symbol

    def move_up(self):
        if self.tick_counter % self.speed == 0:
            self.side = 'u'
            if self.y > 0:
                if isinstance(self.map.body_layer[self.y - 1][self.x], BaseEntity):
                   self.map.body_layer[self.y - 1][self.x].move_up()
                elif not self.map.body_layer[self.y - 1][self.x].opaque:
                    self.map.body_layer[self.y][self.x] = self.inside_block
                    self.inside_block = self.map.body_layer[self.y - 1][self.x]
                    self.map.body_layer[self.y - 1][self.x] = self
                    self.y = self.y - 1

    def move_down(self):
        if self.tick_counter % self.speed == 0:
            self.side = 'd'
            if self.y < self.map.height - 1:
                if isinstance(self.map.body_layer[self.y + 1][self.x], BaseEntity):
                   self.map.body_layer[self.y + 1][self.x].move_down()
                elif not self.map.body_layer[self.y + 1][self.x].opaque:
                    self.map.body_layer[self.y][self.x] = self.inside_block
                    self.inside_block = self.map.body_layer[self.y + 1][self.x]
                    self.map.body_layer[self.y + 1][self.x] = self
                    self.y = self.y + 1

    def move_left(self):
        if self.tick_counter % self.speed == 0:
            self.side = 'l'
            if self.x > 0:
                if isinstance(self.map.body_layer[self.y][self.x - 1], BaseEntity):
                   self.map.body_layer[self.y][self.x - 1].move_left()
                elif not self.map.body_layer[self.y][self.x - 1].opaque:
                    self.map.body_layer[self.y][self.x] = self.inside_block
                    self.inside_block = self.map.body_layer[self.y][self.x - 1]
                    self.map.body_layer[self.y][self.x - 1] = self
                    self.x = self.x - 1

    def move_right(self):
        if self.tick_counter % self.speed == 0:
            self.side = 'r'
            if self.x < self.map.width - 1:
                if isinstance(self.map.body_layer[self.y][self.x + 1], BaseEntity):
                   self.map.body_layer[self.y][self.x + 1].move_right()
                elif not self.map.body_layer[self.y][self.x + 1].opaque:
                    self.map.body_layer[self.y][self.x] = self.inside_block
                    self.inside_block = self.map.body_layer[self.y][self.x + 1]
                    self.map.body_layer[self.y][self.x + 1] = self
                    self.x = self.x + 1

    def tick(self):
        if self.tick_counter < 2147483647:
            self.tick_counter += 1
        else:
            self.tick_counter = 0