class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if self.stack:
            top_elm = self.stack[0]
            min_val = top_elm[1] if top_elm[1] < val else val
            self.stack.insert(0, (val, min_val))
        else:
            self.stack.insert(0, (val, val))
            
            
    def pop(self) -> None:
        if self.stack:
            elm = self.stack.pop(0)
       

    def top(self) -> int:
        if self.stack:
            top_elm = self.stack[0]
            return top_elm[0]
        return None

    def getMin(self) -> int:
        if self.stack:
            top_elm = self.stack[0]
            return top_elm[1]
        return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()