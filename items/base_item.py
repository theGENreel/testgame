from abc import abstractmethod
from typing import Type

from blocks.base_block import BaseBlock


class BaseItem:
    def __init__(self):
        self.interactable = False
        self.placeable = False
        self.block = None
        self.name = 'Item'

    def __str__(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def set_interactable(self, interactable):
        self.interactable = interactable

    def set_placeable(self, placeable, block: Type[BaseBlock]):
        self.placeable = placeable
        self.block = block

    @abstractmethod
    def on_interact(self, initiator):
        pass

    def __eq__(self, other):
        if isinstance(other, str):
            return True if self.name == other else False
        elif isinstance(other, BaseItem):
            return True if self.name == other.name else False
        else:
            return False
