class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        current_min = self.min_stack[-1] if self.min_stack else val
        new_min = min(val, current_min)
        self.min_stack.append(new_min)
        

    def pop(self) -> None:
        if not self.stack:
            return
        
        last_element =  self.stack.pop()
        self.min_stack.pop()
        return last_element
        

    def top(self) -> int:
        if not self.stack:
            return
        
        return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.min_stack:
            return "null"
        
        return self.min_stack[-1]
