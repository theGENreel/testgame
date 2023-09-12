from items.base_item import BaseItem


class Slot:
    def __init__(self, max_size: int = 64, item: BaseItem = None, count: int = 0):
        self.max_size = max_size
        self.item = item
        self.count = count

    def add_item(self, item: BaseItem, count: int):
        if self.item is None:
            self.item = item
        if self.item == item:
            if self.count + count <= self.max_size:
                self.count += count
                return True
        return False

    def is_filled(self) -> bool:
        return False if self.count < self.max_size else True

    def remain_count(self) -> int:
        return self.max_size - self.count

    def merge_slot(self, ext_slot: "Slot", count: int = None):
        if count is None and ext_slot.count > 0:
            if self.item is None:
                self.item = ext_slot.item
            if self.item == ext_slot.item:
                if self.count + ext_slot.count <= self.max_size:
                    self.count += ext_slot.count
                    ext_slot.count = 0
                    ext_slot.item = None
                else:
                    ext_slot.count -= self.max_size - self.count
                    self.count = self.max_size
                return True
        elif count is not None and ext_slot.count > 0:
            if self.item is None:
                self.item = ext_slot.item
            if self.item == ext_slot.item:
                if self.count + count <= self.max_size:
                    self.count += count
                    ext_slot.count -= count
                    if ext_slot.count == 0:
                        ext_slot.item = None
                else:
                    ext_slot.count -= self.max_size - self.count
                    self.count = self.max_size
                return True
        return False

    def get_count(self):
        return self.count

    def get_max_size(self):
        return self.max_size
