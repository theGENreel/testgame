from abc import abstractmethod


class BaseBlock:
    def __init__(self):
        self.opaque = False
        self.ticking = False
        self.interactable = False
        self.symbol = ' '

    def __str__(self):
        return self.symbol

    # If set, entity can't go through block
    def set_opaque(self, opaque: bool):
        self.opaque = opaque

    # Sets symbol for draw
    def set_symbol(self, symbol: chr):
        self.symbol = symbol

    def set_ticking(self, ticking: bool):
        self.ticking = ticking

    def is_ticking(self):
        return self.ticking

    def set_interactable(self, interactable):
        self.interactable = interactable

    def tick(self):
        pass

    def on_place(self, side_blocks: dict, initiator=None):
        pass

    def on_interact(self, initiator):
        pass
