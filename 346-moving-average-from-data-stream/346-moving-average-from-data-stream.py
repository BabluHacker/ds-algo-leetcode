class MovingAverage:

    def __init__(self, size: int):
        self.arr = []
        self.size = size
        self.curr_size = 0

    def next(self, val: int) -> float:
        if len(self.arr) >= self.size:
            self.arr.pop(0)
            self.curr_size -= 1
        self.arr.append(val)
        self.curr_size += 1
        
        return sum(self.arr) / self.curr_size 
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)