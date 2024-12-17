import collections
"""
12.1 Can from a palindrome permutation
"""
def can_form_palindrome(s: str):
    print(collections.Counter(s))
    print(collections.Counter(s).values())
    print(sum(v % 2 for v in collections.Counter(s).values()))
    return sum(v % 2 for v in collections.Counter(s).values()) <= 1


can_form_palindrome('edified')

"""
Check if characters from string can be use to anonymize letter
Time: O(m+n) m, n are length of letter and magazine
Space: O(c) c is number of distinct characters in letter
"""
def is_letter_constructible_from_magazine(letter_text: str, magazine_text: str) -> bool:
    return (not collections.Counter(letter_text) - collections.Counter(magazine_text))

"""
ISBN cache, LRU cache
"""

class LRUCache:
    def __init__(self, capacity: int):
        self.price_table = collections.OrderedDict()
        self.capacity = capacity
    
    def lookup(self, isbn):
        if isbn not in self.price_table:
            return -1
        price = self.price_table.pop(isbn)
        self.price_table[isbn] = price
        return price
    
    def insert(self, isbn):
        if isbn not in self.price_table:
            return -1

        price = self.price_table.pop(isbn)
        self.price_table[isbn] = price
        return price
    
    def insert(self, isbn, price):
        if isbn in self.price_table:
            price = self.price_table.pop(isbn)
        elif self.capacity <= len(self.price_table):
            # remove the first item (oldest) that was inserted
            self.price_table.popitem(last=False)  
            self.price_table[isbn] = price
        return price


# Reviewed on Dec 16, 2024
class LRUCache:
    def __init__(self, capacity: int):
        self.store = collections.OrderedDict()
        self.capacity = capacity
    
    def lookup(self, key):
        if key not in self.store:
            return -1
        value = self.store.pop(key)
        self.store[key] = value
        return value
    
    def insert(self, key, value):
        if key in self.store:
            value = self.store.pop(key)
        elif self.capacity <= len(self.store):
            # pop the oldes item, which is the first item
            self.store.popitem(last=False)
            self.store[key] = value
        return value

    def erase(self, key):
        return self.store.pop(key, None) is not None