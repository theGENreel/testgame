from blocks.base_block import BaseBlock


class Pipe(BaseBlock):
    symbols = {'ur': '╚', 'ul': '╝', 'dr': '╔', 'dl': '╗', 'lr': '═', 'ud': '║', 'udl': '╣', 'udr': '╠', 'ulr': '╩',
             'dlr': '╦', 'udlr': '╬'}
    def __init__(self):
        super().__init__()
        self.set_interactable(True)
        self.sides = {'up': False, 'down': False, 'left': False, 'right': False}
        self.update_sides()
        self.set_ticking(True)

    def tick(self):
        pass

    def update_sides(self):
        s = ''
        if self.sides['up']:
            s += 'u'
        if self.sides['down']:
            s += 'd'
        if self.sides['left']:
            s += 'l'
        if self.sides['right']:
            s += 'r'
        if s == '':
            s = 'lr'
        if len(s) == 1:
            if s == 'r' or s == 'l':
                s = 'lr'
            elif s == 'u' or s == 'd':
                s = 'ud'
        self.symbol = self.symbols[s]

    def set_side(self, side: str, status: bool):
        if side == 'up' or side == 'down' or side == 'left' or side == 'right':
            self.sides[side] = status
        self.update_sides()

    def on_interact(self, initiator):
        pass

    def on_place(self, side_blocks: dict, initiator=None):
        if isinstance(side_blocks['l'], Pipe):
            self.set_side('left', True)
            side_blocks['l'].set_side('right', True)
        if isinstance(side_blocks['r'], Pipe):
            self.set_side('right', True)
            side_blocks['r'].set_side('left', True)
        if isinstance(side_blocks['u'], Pipe):
            self.set_side('up', True)
            side_blocks['u'].set_side('down', True)
        if isinstance(side_blocks['d'], Pipe):
            self.set_side('down', True)
            side_blocks['d'].set_side('up', True)
