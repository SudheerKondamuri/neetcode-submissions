class MyHashSet:

    def __init__(self):
        self.hashset = []
        

    def add(self, key: int) -> None:
        if key in self.hashset :
            return
        self.hashset.append(key)
        

    def remove(self, key: int) -> None:
        k = 0 
        for i in range(len(self.hashset)) :
            if self.hashset[i] != key :
                self.hashset[k] = self.hashset[i]
                k += 1
        self.hashset = self.hashset[:k]
        

    def contains(self, key: int) -> bool:
        return True if key in self.hashset else False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)