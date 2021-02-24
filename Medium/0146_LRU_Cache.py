# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
# Implement the LRUCache class:
#
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache.
# If the number of keys exceeds the capacity from this operation,
# evict the least recently used key.

class LRUCache:

    def __init__(self, capacity: int):
        self.cache_key = []
        self.cache_val = []
        self.cache_cap = capacity

    def get(self, key: int) -> int:
        if key in self.cache_key:
            index = self.cache_key.index(key)
            self.cache_key.append(self.cache_key.pop(index))
            self.cache_val.append(self.cache_val.pop(index))
            return self.cache_val[-1]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache_key:
            index = self.cache_key.index(key)
            self.cache_key.append(self.cache_key.pop(index))
            self.cache_val.append(self.cache_val.pop(index))
            self.cache_val[-1] = value

        else:
            if len(self.cache_key) < self.cache_cap:
                self.cache_key.append(key)
                self.cache_val.append(value)
            else:
                self.cache_key.append(key)
                self.cache_val.append(value)
                self.cache_key.pop(0)
                self.cache_val.pop(0)
        return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


