from blocks.base_block import BaseBlock


class Pipe(BaseBlock):
    symbols = {'ur': '╚', 'ul': '╝', 'dr': '╔', 'dl': '╗', 'lr': '═', 'ud': '║', 'udl': '╣', 'udr': '╠', 'ulr': '╩',
             'dlr': '╦', 'udlr': '╬'}
    def __init__(self, side: str):
        super().__init__()
        self.set_interactable(True)
        self.sides = {'up': False, 'down': False, 'left': False, 'right': False}

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
        self.symbol = self.symbols[s]

    def set_side(self, side: str, status: bool):
        if side == 'up' or side == 'down' or side == 'left' or side == 'right':
            self.sides[side] = status
        self.update_sides()

    def on_interact(self, initiator):
        pass

    def on_place(self, initiator=None):
        pass
