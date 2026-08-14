class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tt = temperatures
        N = len(tt)

        res = [0]*N
        s = []

        for i in range(N):
            while s and tt[i] > s[-1][0]:
                _, si = s.pop()
                res[si] = i-si
            s.append((tt[i], i))
        return res

            