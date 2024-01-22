from perlin_noise import PerlinNoise

from blocks.pipe import Pipe
from entities.player import EntityPlayer
from fblocks.fstone import StoneFBlock
from blocks.air import Air
from blocks.stone import Stone
from fblocks.firon_ore import FIronOre
from fblocks.fcopper_ore import FCopperOre
from fblocks.fcoal_ore import FCoalOre
from fblocks.fore import FOre
from entities.mobs.base_mob import BaseMob


class Map:
    def __init__(self, width, height):
        self.player = None
        self.width = width
        self.height = height
        self.floor_layer = []
        self.body_layer = []
        self.ticking_blocks = []
        self.ticking_mobs = []

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
        self.generate_ore(FCoalOre, 0.4, 1000, 8)

        self.body_layer[14][2] = BaseMob(self, '$', 2, 14)
        self.ticking_mobs.append(self.body_layer[14][2])

    def add_player(self, player: EntityPlayer):
        self.player = player
        self.body_layer[self.player.x][self.player.y] = self.player

    def generate_ore(self, ore, cut: float, freq_divider: int, seed: int):
        noise = PerlinNoise(octaves=20, seed=seed)
        for x, line in enumerate(self.floor_layer):
            for y, block in enumerate(line):
                if noise([x / freq_divider, y / freq_divider]) <= cut * -1:
                    self.floor_layer[x][y] = ore()
