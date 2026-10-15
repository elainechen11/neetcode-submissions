class MyHashSet:

    def __init__(self):
        self.liste = []

    def add(self, key: int) -> None:
        self.liste.append(key)

    def remove(self, key: int) -> None:
        i = 0
        while i < len(self.liste):
            if self.liste[i] == key:
                self.liste.pop(i)
            else:
                i += 1

    def contains(self, key: int) -> bool:
        if self.liste == []:
            return False
        for num in self.liste:
            if num == key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)