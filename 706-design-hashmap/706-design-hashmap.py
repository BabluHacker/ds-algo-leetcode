class MyHashMap:

    def __init__(self):
        self.data = {}
        
    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        if key in self.data:
            return self.data[key]
        return -1

    def remove(self, key: int) -> None:
        if key in self.data:
            del self.data[key] 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)