from abc import abstractmethod


class BaseFBlock:
    def __init__(self):
        self.interactable = False
        self.symbol = '░'

    def __str__(self):
        return self.symbol

    def set_symbol(self, symbol: chr):
        self.symbol = symbol

    def set_interactable(self, interactable):
        self.interactable = interactable

    @abstractmethod
    def on_interact(self, initiator):
        pass
