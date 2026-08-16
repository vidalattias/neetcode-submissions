class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper_bound = max(piles)

        def compute_time(k):
            t = 0
            for p in piles:
                t += -(-p//k)
            return t

        def aux(i, j):
            if i > j:
                return (False, None)
            if i == j:
                t = compute_time(i)
                if t <= h:
                    return (True, i)
                else:
                    return (False, None)

            mid = i + (j-i+1)//2
            t = compute_time(mid)
            if t > h:
                # must increase k
                new_i = mid + 1
                new_j = j
                return aux(new_i, new_j)
            elif t <= h:
                new_i = i
                new_j = mid -1
                boolean, index = aux(new_i, new_j)
                if boolean:
                    return (True, index)
                else:
                    return (True, mid)

        m = max(piles)
        boolean, value = aux(1, m)
        return value

