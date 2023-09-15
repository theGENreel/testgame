from perlin_noise import PerlinNoise

from blocks.pipe import Pipe
from fblocks.fstone import StoneFBlock
from blocks.air import Air
from blocks.stone import Stone
from fblocks.firon_ore import FIronOre
from fblocks.fcopper_ore import FCopperOre
from fblocks.fcoal_ore import FCoalOre
from player import Player


class Map:
    def __init__(self, width, height):
        self.player = None
        self.width = width
        self.height = height
        self.floor_layer = []
        self.body_layer = []
        self.ticking_blocks = []

        for line in range(height):
            self.body_layer.append([])
            self.floor_layer.append([])
            # Fill floor with stone and body with air
            for column in range(width):
                self.body_layer[len(self.body_layer)-1].append(Air())
                self.floor_layer[len(self.floor_layer) - 1].append(StoneFBlock())
        self.body_layer[3][5] = Stone()
        self.body_layer[10][10] = Stone()
        self.body_layer[11][10] = Stone()
        self.body_layer[12][10] = Stone()
        self.body_layer[12][11] = Stone()
        self.body_layer[10][11] = Stone()
        self.body_layer[10][12] = Stone()
        self.body_layer[11][12] = Stone()
        self.body_layer[12][12] = Stone()
        self.floor_layer[2][3] = FIronOre()
        self.floor_layer[3][3] = FIronOre()
        self.floor_layer[4][3] = FIronOre()
        self.floor_layer[2][5] = FCopperOre()
        self.floor_layer[3][5] = FCopperOre()
        self.floor_layer[4][5] = FCopperOre()
        self.floor_layer[2][7] = FCoalOre()
        self.floor_layer[3][7] = FCoalOre()
        self.floor_layer[4][7] = FCoalOre()
        self.body_layer[1][9] = Pipe()
        self.body_layer[2][9] = Pipe()
        self.body_layer[3][9] = Pipe()
        self.body_layer[4][9] = Pipe()
        self.body_layer[5][9] = Pipe()
        self.body_layer[5][10] = Pipe()
        self.body_layer[5][11] = Pipe()
        self.body_layer[5][12] = Pipe()
        self.body_layer[5][13] = Pipe()
        self.body_layer[4][13] = Pipe()
        self.body_layer[3][13] = Pipe()
        self.body_layer[2][13] = Pipe()
        self.body_layer[1][13] = Pipe()
        self.body_layer[1][12] = Pipe()
        self.body_layer[1][11] = Pipe()
        self.body_layer[1][10] = Pipe()
        # Creating player
        self.debug_str = ''
        self.generate_ores(1)

    def add_player(self, player: Player):
        self.player = player
        self.body_layer[self.player.x][self.player.y] = self.player

    def generate_ores(self, seed: int):
        noise = PerlinNoise(octaves=20, seed=seed)
        # xpix, ypix = 128, 128
        for x, line in enumerate(self.floor_layer):
            for y, block in enumerate(line):
                if noise([x / self.width, y / self.height]) <= -0.55:
                    self.floor_layer[x][y] = FCoalOre()
        # pic = [[1 if noise([i / xpix, j / ypix]) > -0.4 else 0 for j in range(xpix)] for i in range(ypix)]
