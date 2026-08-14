import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for t in tokens:
            if t in '+*/-':
                r = s.pop()
                l = s.pop()

                if t == '+':
                    tmp = l+r
                elif t == '-':
                    tmp = l-r
                elif t == '*':
                    tmp = l*r
                elif t == '/':
                    tmp = int(l/r)
            else:
                tmp = int(t)
            s.append(tmp)

        return tmp