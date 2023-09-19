from blocks.air import Air


class BaseMob:
    def __init__(self, map: "Map", symbol: str, x: int, y: int):
        self.map = map
        self.symbol = symbol
        self.x = x
        self.y = y
        self.side = 'r'
        self.inside_block = Air()

    def __str__(self):
        return self.symbol

    def move_up(self):
        self.side = 'u'
        if self.y > 0:
            if not self.map.body_layer[self.y - 1][self.x].opaque:
                self.map.body_layer[self.y][self.x] = self.inside_block
                self.inside_block = self.map.body_layer[self.y - 1][self.x]
                self.map.body_layer[self.y - 1][self.x] = self
                self.y = self.y - 1

    def move_down(self):
        self.side = 'd'
        if self.y < self.map.height - 1:
            if not self.map.body_layer[self.y + 1][self.x].opaque:
                self.map.body_layer[self.y][self.x] = self.inside_block
                self.inside_block = self.map.body_layer[self.y + 1][self.x]
                self.map.body_layer[self.y + 1][self.x] = self
                self.y = self.y + 1

    def move_left(self):
        self.side = 'l'
        if self.x > 0:
            if not self.map.body_layer[self.y][self.x - 1].opaque:
                self.map.body_layer[self.y][self.x] = self.inside_block
                self.inside_block = self.map.body_layer[self.y][self.x - 1]
                self.map.body_layer[self.y][self.x - 1] = self
                self.x = self.x - 1

    def move_right(self):
        self.side = 'r'
        if self.x < self.map.width - 1:
            if not self.map.body_layer[self.y][self.x + 1].opaque:
                self.map.body_layer[self.y][self.x] = self.inside_block
                self.inside_block = self.map.body_layer[self.y][self.x + 1]
                self.map.body_layer[self.y][self.x + 1] = self
                self.x = self.x + 1

    def tick(self):
        pass