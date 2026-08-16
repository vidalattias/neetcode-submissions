class Stack:
    def __init__(self):
        self.s = []
    
    def push(self, x):
        self.s.append(x)
    
    def peek(self):
        return self.s[-1]
    
    def pop(self):
        return self.s.pop()

    def size(self):
        return len(self.s)
    
    def is_empty(self):
        return len(self.s) == 0

class MyQueue:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x: int) -> None:
        self.s1.push(x)

    def pop(self) -> int:
        sz = self.s1.size()

        for _ in range(sz):
            val = self.s1.pop()
            self.s2.push(val)
        
        self.s2.pop()
        for _ in range(sz-1):
            tmp = self.s2.pop()
            self.s1.push(tmp)
        
        return val

    def peek(self) -> int:
        sz = self.s1.size()

        for _ in range(sz):
            val = self.s1.pop()
            self.s2.push(val)
        
        for _ in range(sz):
            tmp = self.s2.pop()
            self.s1.push(tmp)
        
        return val

    def empty(self) -> bool:
        return self.s1.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()