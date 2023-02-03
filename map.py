from fblocks.fstone import StoneFBlock
from blocks.air import Air
from blocks.stone import Stone
from fblocks.firon_ore import FIronOre
from player import Player


class Map:
    def __init__(self, width, height, player=None):
        self.width = width
        self.height = height
        self.player = player if player is not None else Player()
        self.floor_layer = []
        self.body_layer = []

        for line in range(height):
            self.body_layer.append([])
            self.floor_layer.append([])
            # Fill floor with stone and body with air
            for column in range(width):
                self.body_layer[len(self.body_layer)-1].append(Air())
                self.floor_layer[len(self.floor_layer) - 1].append(StoneFBlock())
        self.body_layer[10][10] = Stone()
        self.body_layer[11][10] = Stone()
        self.body_layer[12][10] = Stone()
        self.body_layer[12][11] = Stone()
        self.body_layer[10][11] = Stone()
        self.body_layer[10][12] = Stone()
        self.body_layer[11][12] = Stone()
        self.body_layer[12][12] = Stone()
        self.floor_layer[2][2] = FIronOre()
        self.floor_layer[2][3] = FIronOre()
        self.floor_layer[3][2] = FIronOre()
        self.floor_layer[3][3] = FIronOre()
        # Creating player
        self.body_layer[self.player.x][self.player.y] = self.player
        self.debug_str = ''

    def input(self, key):
        # Player Movement
        if key == ord('W') or key == ord('S') or key == ord('A') or key == ord('D') or key == ord('w') or key == ord(
                's') or key == ord('a') or key == ord('d'):
            if key == ord('W') or key == ord('w'):
                if self.player.y > 0:
                    if not self.body_layer[self.player.x][self.player.y - 1].opaque:
                        self.body_layer[self.player.y - 1][self.player.x] = self.player
                        self.body_layer[self.player.y][self.player.x] = Air()
                        self.player.y = self.player.y - 1
            elif key == ord('S') or key == ord('s'):
                if self.player.y < self.height - 1:
                    if not self.body_layer[self.player.x][self.player.y + 1].opaque:
                        self.body_layer[self.player.y + 1][self.player.x] = self.player
                        self.body_layer[self.player.y][self.player.x] = Air()
                        self.player.y = self.player.y + 1
            elif key == ord('A') or key == ord('a'):
                if self.player.x > 0:
                    if not self.body_layer[self.player.x - 1][self.player.y].opaque:
                        self.body_layer[self.player.y][self.player.x - 1] = self.player
                        self.body_layer[self.player.y][self.player.x] = Air()
                        self.player.x = self.player.x - 1
            elif key == ord('D') or key == ord('d'):
                if self.player.x < self.width - 1:
                    if not self.body_layer[self.player.x + 1][self.player.y].opaque:
                        self.body_layer[self.player.y][self.player.x + 1] = self.player
                        self.body_layer[self.player.y][self.player.x] = Air()
                        self.player.x = self.player.x + 1
        elif key == ord('E') or key == ord('e'):
            self.debug_str += 'Interact pressed\n'
            if self.floor_layer[self.player.y][self.player.x].interactable:
                self.debug_str += 'Interact\n'
                self.floor_layer[self.player.y][self.player.x].on_interact(self.player)
