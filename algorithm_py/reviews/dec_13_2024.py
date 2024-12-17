"""
LRU Cache
"""

class LRUCache:
    def __init__(self, capacity):
        self.table = collections.OrderedDict # keep track of inserted order
        self.capacity = capacity

    def lookup(self, key):
        if key not in self.table:
            return -1
        value = self.table.pop(key)
        self.table[key] = value
        return value

    def insert(self, key, value):
        if key in self.table:
            value = self.table.pop(key)
        elif self.capacity <= len(self.table):
            self.table.popitem(last=False)

        self.table[key] = value
        return value

    def erase(self, key):
        return self.table.pop(key, None) is not None
