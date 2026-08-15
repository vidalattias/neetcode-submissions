class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        for o in operations:
            if o == "+":
                last = s.pop()
                last_last = s.pop()
                s.append(last_last)
                s.append(last)
                s.append(last+last_last)
            elif o == 'D':
                last = s.pop()
                s.append(last)
                s.append(2*last)
            elif o == 'C':
                s.pop()
            else:
                print(o)
                s.append(int(o))

        summation = 0
        while s:
            last = s.pop()
            summation += last
        return summation