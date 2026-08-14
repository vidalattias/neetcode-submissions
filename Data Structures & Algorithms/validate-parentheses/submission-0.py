class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x in '{([':
                print("Found!")
                stack.append(x)

            if x in '})]':
                cmp = {
                    '}' : '{',
                    ')' : '(',
                    ']' : '[',
                }[x]
                if len(stack) == 0:
                    return False
                if stack.pop() != cmp:
                    return False
            
        return (len(stack) == 0)