class MinStack:

    def __init__(self):
        self.s = []
        self.min_s = []

    def push(self, val: int) -> None:
        self.s.append(val)

        if self.min_s:
            current_min = min(self.min_s[-1], val)
        else:
            current_min = val
        self.min_s.append(current_min)

    def pop(self) -> None:
        self.min_s.pop()
        return self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min_s[-1]
