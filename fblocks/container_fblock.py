from fblocks.base_fblock import BaseFBlock


class FContainer(BaseFBlock):
    def __init__(self, slots: int):
        super().__init__()
        self.slots = []
        self.slots_count = slots

    def on_interact(self, initiator):
        initiator.give_item()
