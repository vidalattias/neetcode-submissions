class Solution:
    def isValid(self, s: str) -> bool:
        ss = []

        for x in s:
            if x in '{([':
                ss.append(x)
            if x in '}])':
                if not ss:
                    return False
                last = ss.pop()
                if last != {'}':'{', ']':'[', ')':'('}[x]:
                    return False
        return len(ss) == 0