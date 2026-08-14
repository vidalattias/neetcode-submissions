class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        N = len(position)
        order = sorted([(p, i) for i,p in enumerate(position)])

        n_p = [position[i] for _,i in order]
        n_s = [speed[i] for _,i in order]

        arrivals = [0]*N

        for i in range(N-1, -1, -1):
            theo_time = (target-n_p[i])/n_s[i]
            if i < N-1:
                if theo_time < arrivals[i+1]:
                    theo_time = arrivals[i+1]
            arrivals[i] = theo_time

        return len(set(arrivals))