from typing import Dict


class Inventory:
    def __init__(self, initial=None):
        self.items = {}
        for item, amount in initial.items():
            self.items[item] = amount
    def display_inventory(self):
        for key, value in self.items.items():
            print(value, key)
    def add_to_inventory(self, append_items) -> None:
        for increment in append_items:
            self.items[increment] = self.items.get(increment, 0) + 1

testinv = Inventory({'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12 })
testinv.display_inventory()
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
testinv.add_to_inventory(dragonLoot)
testinv.display_inventory()