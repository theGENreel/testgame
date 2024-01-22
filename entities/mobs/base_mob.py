from blocks.air import Air
from entities.base_entity import BaseEntity
from entities.player import EntityPlayer


class BaseMob(BaseEntity):
    def __init__(self, map: "Map", symbol: str, x: int, y: int):
        super().__init__(map, symbol, x, y)
        self.distance_of_view = 15

    def tick(self):
        super().tick()
        for x in range(self.distance_of_view * -1, self.distance_of_view):
            for y in range(self.distance_of_view * -1, self.distance_of_view):
                if 0 <= self.x + x < self.map.width and 0 <= self.y + y < self.map.height and type(self.map.body_layer[self.x + x][self.y + y]) == EntityPlayer:
                    if x < 0:
                        self.move_left()
                    elif x > 0:
                        self.move_right()
                    if y < 0:
                        self.move_up()
                    elif y > 0:
                        self.move_down()