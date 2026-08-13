class Solution:
    def trap(self, height: List[int]) -> int:
        h = height
        N = len(h)

        l = 0
        lm = h[l]

        r = N-1
        rm = h[r]

        res = 0

        while l < r:
            if lm<rm:
                l += 1
                lm = max(lm, h[l])
                res += lm-h[l]
            else:
                r -= 1
                rm = max(rm, h[r])
                res += rm-h[r]
        return res
