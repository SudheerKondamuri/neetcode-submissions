class MyHashMap:


    def __init__(self):
        # Start with None to represent a truly empty slot
        self.storage = [None] * 1000001

    def put(self, key: int, value: int) -> None:
        self.storage[key] = value

    def get(self, key: int) -> int:
        # If the slot is None, the key does not exist. Return -1.
        if self.storage[key] is None:
            return -1
        # Otherwise, return the actual value (even if the value is -1!)
        return self.storage[key]

    def remove(self, key: int) -> None:
        # Truly delete the key by wiping it back to None
        self.storage[key] = None



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)