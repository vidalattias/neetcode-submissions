class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tt = temperatures
        N = len(tt)

        res = [0]*N

        for i in range(N-2, -1, -1):
            j = i+1

            while j < N and tt[j] <= tt[i]:
                if res[j] == 0:
                    j = None
                    break
                else:
                    j += res[j]

            if j:
                res[i] = j-i
        return res

            