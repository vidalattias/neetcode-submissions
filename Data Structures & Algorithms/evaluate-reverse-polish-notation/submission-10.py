import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t in '+-*/':
                ro = s.pop()
                lo = s.pop()
                if t == '+':
                    tmp = lo + ro
                elif t == '-':
                    tmp = lo - ro
                elif t == '*':
                    tmp = lo * ro
                elif t == '/':
                    tmp = int(lo / ro)

            else:
                tmp = int(t)

            s.append(tmp)
            #print(f'Exiting - {s}\n')
        return s.pop()