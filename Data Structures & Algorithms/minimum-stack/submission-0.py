class MinStack:

    def __init__(self):
        self.stack=[]
        self.minval=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minval:
            self.minval.append(val)
        else:
            self.minval.append(min(self.minval[-1],val))
        

    def pop(self) -> None:
        self.stack.pop()
        self.minval.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minval[-1]
        
