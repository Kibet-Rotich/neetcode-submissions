class MinStack:

    def __init__(self):
        self.items = []
        
        

    def push(self, val: int) -> None:
        minimum= min(self.items[-1][1], val)  if self.items else val
        self.items.append((val,minimum))
        

    def pop(self) -> None:
        return self.items.pop() if self.items else None
        

    def top(self) -> int:
        return self.items[-1][0] if self.items else None
        

    def getMin(self) -> int:
        return self.items[-1][1] if self.items else None

        
