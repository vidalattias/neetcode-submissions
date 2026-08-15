class Solution:
    def minOperations(self, logs: List[str]) -> int:
        s = []
        for l in logs:
            if l == './':
                continue
            elif l == '../':
                if s:
                    s.pop()
            else:
                s.append(l)

        res = 0
        while s:
            s.pop()
            res+=1
        return res