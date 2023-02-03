from blocks.base_block import BaseBlock


class Stone(BaseBlock):
    def __init__(self):
        super().__init__()
        self.set_opaque(True)
        self.set_symbol('#')
