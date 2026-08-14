class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tt = temperatures
        N = len(tt)

        s = []
        res = [0]*N

        for i, t in enumerate(tt):
            while s and t > s[-1][0]:
                _, si = s.pop()
                res[si] = i-si
            s.append((t, i))

        return res