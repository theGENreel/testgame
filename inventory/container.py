from inventory.slot import Slot
from items.base_item import BaseItem


class Container:
    def __init__(self, slots: int):
        self.slots = [Slot() for i in range(slots)]

    def get_items(self) -> list:
        return [slot.item for slot in self.slots]

    def has_empty_slots(self) -> bool:
        items = self.get_items()
        return True if None in items else False

    def get_empty_slot(self) -> Slot|None:
        if self.has_empty_slots():
            return self.slots[self.get_items().index(None)]
        return None

    def get_occupied(self) -> list:
        return [slot for slot in self.slots if slot.item is not None]

    def get_slot_for_item(self, item_ext: BaseItem) -> Slot|None:
        items = self.get_items()
        for idx, item in enumerate(items):
            if item == item_ext and self.slots[idx].count < self.slots[idx].max_size:
                return self.slots[idx]
        return self.get_empty_slot()


    def merge_slot(self, ext_slot: Slot, count: int = None):
        ext_count = ext_slot.count
        if count is not None and ext_count < count:
            count = ext_count
        if ext_slot.count > 0:
            while (ext_slot.count > 0) if count is None else (ext_slot.count > ext_count - count):
                slot = self.get_slot_for_item(ext_slot.item)
                if slot is None:
                    break
                slot.merge_slot(ext_slot, count)

    def has_items(self, ext_item: BaseItem, count: int):
        items = self.get_items()
        found_count = 0
        for idx, item in enumerate(items):
            if item == ext_item:
                found_count += self.slots[idx].count
        return True if found_count >= count else False

    def remove_items(self, ext_item: BaseItem, count: int):
        while count > 0:
            if not self.has_items(ext_item, count):
                break
            items = self.get_items()
            for idx, item in enumerate(items):
                if item == ext_item:
                    if count >= self.slots[idx].count:
                        count -= self.slots[idx].count
                        self.slots[idx].count = 0
                        self.slots[idx].item = None
                    else:
                        self.slots[idx].count -= count

    def add_items(self, ext_item: BaseItem, count: int): #  TODO: Allow to add items in >1 slots
        slot = Slot(max_size=count, item=ext_item, count=count)
        self.merge_slot(slot)
        # items = self.get_items()
        # while count > 0:
        #     for idx, item in enumerate(items):
        #         if item == ext_item and not self.slots[idx].is_filled():
        #             # count -= self.slots[idx].remain_count()
        #             if count >= self.slots[idx].remain_count():
        #                 count -= self.slots[idx].remain_count()
        #                 self.slots[idx].count = self.slots[idx].max_size
        #             else:
        #                 self.slots[idx].count += count
        #                 count = 0
        #                 return


        # if ext_item in items:
        #     self.slots[items.index(ext_item)].add_item(ext_item, count)

