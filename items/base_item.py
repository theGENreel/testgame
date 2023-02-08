from abc import abstractmethod


class BaseItem:
    def __init__(self, count=1):
        self.interactable = False
        self.name = 'Item'
        self.count = count

    def __str__(self):
        return self.name

    def __int__(self):
        return self.count

    def __add__(self, other):
        self.count += other.count

    def __sub__(self, other):
        self.count -= other

    def __divmod__(self, other):
        self.count /= other

    def __mul__(self, other):
        self.count *= other

    def set_name(self, name: str):
        self.name = name

    def set_interactable(self, interactable):
        self.interactable = interactable

    def set_count(self, count):
        self.count = count

    @abstractmethod
    def on_interact(self, initiator):
        pass
