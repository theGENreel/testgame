class BaseBlock:
    def __init__(self):
        self.opaque = False
        self.symbol = ' '

    def __str__(self):
        return self.symbol

    # If set, entity can't go through block
    def set_opaque(self, opaque: bool):
        self.opaque = opaque

    # Sets symbol for draw
    def set_symbol(self, symbol: chr):
        self.symbol = symbol
