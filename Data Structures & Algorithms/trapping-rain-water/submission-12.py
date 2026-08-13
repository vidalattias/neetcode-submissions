class Solution:
    def trap(self, height: List[int]) -> int:
        h = height
        N = len(h)

        l = 0
        r = N-1

        lm = h[l]
        rm = h[r]

        res = 0

        while(l<r):
            if lm < rm:
                l += 1
                lm = max(lm, h[l])
                res += lm - h[l]
                #print(f'Moved l - {res} ({lm};{rm};{l};{r};{h[l]})')
            else:
                r -= 1
                rm = max(rm, h[r])
                res += rm - h[r]
                #print(f'Moved r - {res} ({lm};{rm};{l};{r};{h[r]})')
        return res