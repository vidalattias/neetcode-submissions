class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tt = temperatures
        N = len(tt)

        res = [0]*N
        s = []

        for i, t in enumerate(tt):
            while s and t > s[-1][0]:
                tmp = s.pop()
                st, si = tmp[0], tmp[1]
                res[si] = i - si
            s.append([t,i])
        return res