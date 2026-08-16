class MyQueue:
    def __init__(self):
        self.l = []
    
    def push(self, x):
        self.l.append(x)
    
    def peek(self):
        if self.l:
            return self.l[0]
        else:
            raise Exception('Empty queue')

    def pop(self):
        if self.l:
            val = self.l[0]
            self.l = self.l[1:]
            return val
        else:
            raise Exception("Empty queue")

    def size(self):
        return len(self.l)

    def is_empty(self):
        return len(self.l) == 0

    def __str__(self):
        return str(self.l)

class MyStack:

    def __init__(self):
        self.q1 = MyQueue()
        #self.q2 = MyQueue()

    def push(self, x: int) -> None:
        self.q1.push(x)

    def pop(self) -> int:
        #print(f'Pre-pop : {self.q1}')
        sz = self.q1.size()
        for i in range(sz-1):
            val = self.q1.pop()
            self.q1.push(val)
        val = self.q1.pop()
        #print(f'Pop : {val}')
        return val

    def top(self) -> int:
        #print(f'Pre-top : {self.q1}')
        sz = self.q1.size()
        for i in range(sz):
            val = self.q1.pop()
            #print(f'\tval: {val}')
            self.q1.push(val)
        #print(f'Top : {val}')
        return val

    def empty(self) -> bool:
        return self.q1.is_empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()