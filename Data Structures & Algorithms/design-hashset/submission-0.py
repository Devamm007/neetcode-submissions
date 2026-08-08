class MyHashSet:

    def __init__(self):
        self.l = []

    def add(self, key: int) -> None:
        self.l.append(key)

    def remove(self, key: int) -> None:
        i = 0
        while i < len(self.l):
            if self.l[-i-1] == key:
                self.l[-i-1], self.l[-1] == self.l[-1], self.l[-i-1]
                self.l.pop()
                i -= 1
            i += 1



    def contains(self, key: int) -> bool:
        return key in self.l


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)