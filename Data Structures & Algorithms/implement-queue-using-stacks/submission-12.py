class Stack:
    def __init__(self):
        self.s = []
    
    def push(self, x):
        self.s.append(x)

    def peek(self, x):
        return self.s[-1]

    def pop(self):
        val = self.s[-1]
        del self.s[-1]
        return val

    def size(self):
        return len(self.s)

    def is_empty(self):
        return len(self.s) == 0

    def __str__(self):
        return str(self.s)

class MyQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x: int) -> None:
        self.s1.push(x)
        print(f"Pushing {x} - {self.s1}")

    def pop(self) -> int:
        print(f'Pre-pop : {self.s1} - {self.s2}')
        sz = self.s1.size()
        for _ in range(sz):
            print(f'\t{self.s1} - {self.s2}')
            val = self.s1.pop()
            self.s2.push(val)
            print(f'\t{self.s1} - {self.s2}')
            print()

        xx = self.s2.pop()
        print(f'x - {xx}')
        
        for _ in range(sz-1):
            tmp = self.s2.pop()
            self.s1.push(tmp)
        print(f'Post-pop : {self.s1} - {self.s2}')
        return val

    def peek(self) -> int:
        sz = self.s1.size()
        print(f'Pre-peek {self.s1}')
        for _ in range(sz):
            val = self.s1.pop()
            self.s2.push(val)

        #selg.s2.pop()
        print(f'Mid-peek {self.s1} - {self.s2}')
        
        for _ in range(sz):
            tmp = self.s2.pop()
            self.s1.push(tmp)
        
        print(f'Post-peek {self.s1}')
        print()
        return val

    def empty(self) -> bool:
        return self.s1.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()