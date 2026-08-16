class Solution:
    def isValid(self, s: str) -> bool:
        ss = []
        for x in s:
            if x in '{([':
                ss.append(x)
            else:
                if not ss:
                    return False
                if ss.pop() != {'}':'{', ')':'(', ']': '['}[x]:
                    return False
        return len(ss) == 0