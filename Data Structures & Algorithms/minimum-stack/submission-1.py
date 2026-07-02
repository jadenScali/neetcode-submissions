class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        curr_min = self.getMin()
        if curr_min is not None:
            curr_min = min(curr_min, val)
        else:
            curr_min = val

        self.stack.append((val, curr_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return None

        return self.stack[-1][1]
        
