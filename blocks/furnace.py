from blocks.base_block import BaseBlock
from inventory.slot import Slot
from overlays.furnace_overlay import FurnaceOverlay
# from player import Player


class Furnace(BaseBlock):
    def __init__(self):
        super().__init__()
        self.set_interactable(True)
        self.set_ticking(True)
        self.set_opaque(True)
        self.set_symbol('F')
        self.input_slot = Slot()
        self.fuel_slot = Slot()
        self.output_slot = Slot()
        self.current_progress = 0
        self.remain_burn_time = 0

    def tick(self):
        if self.input_slot.count == 0:
            self.input_slot.item = None
            self.current_progress = 0
        if self.fuel_slot.count == 0:
            self.fuel_slot.item = None
        if self.remain_burn_time == 0:
            self.current_progress = 0
        if self.remain_burn_time == 0 and self.fuel_slot.item is not None and self.fuel_slot.item.burn_time > 0:
            self.remain_burn_time = self.fuel_slot.item.burn_time
            self.fuel_slot.count -= 1
        if self.input_slot.item is not None and self.input_slot.item.smelt_time > 0 and self.remain_burn_time > 0:
            self.current_progress += 1
        if self.input_slot.item is not None and self.input_slot.item.smelt_to is not None and self.current_progress >= self.input_slot.item.smelt_time:
            self.output_slot.add_item(self.input_slot.item.smelt_to, 1)
            self.input_slot.count -= 1
            self.current_progress = 0
        if self.remain_burn_time > 0:
            self.remain_burn_time -= 1


    def on_interact(self, initiator):
        # if isinstance(initiator, Player):
        initiator.set_overlay(FurnaceOverlay(initiator.camera, self))

    def on_place(self, side_blocks: dict, initiator=None):
        pass
