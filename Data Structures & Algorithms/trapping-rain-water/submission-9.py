class Solution:
    def trap(self, height: List[int]) -> int:
        h = height
        #h = [4,2,0,3,2,5]
        N = len(h)

        l = 0
        r = N-1

        wl = [0]*N
        wl[0] = h[0]
        wr = [0]*N
        wr[N-1] = h[N-1]

        for i in range(1,N):
            wl[i] = max(wl[i-1], h[i])
            wr[N-i-1] = max(wr[N-i], h[N-i-1])

        s = 0
        for i in range(1, N-1):
            hl = wl[i-1]
            hr = wr[i+1]
            depth = max(0, min(hl, hr)-h[i])
            #print(depth)
            s += depth

        #print(f'{wl=}')
        #print(f'{wr=}')
        #print(f'{s=}')

        return s


