class Solution:
    def maxAreaNaive(self, heights: List[int]) -> int:
        h = heights
        N = len(h)

        max_volume = 0

        for i in range(N):
            for j in range(i+1, N):
                hh = min(h[i], h[j])

                volume = hh * (j-i)
                max_volume = max(volume, max_volume)

        return max_volume

    def maxArea(self, heights: List[int]) -> int:
        h = heights
        N = len(h)

        l = 0
        r = N-1

        volume = min(h[l], h[r]) * (r-l)

        while l < r:
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
            volume = max(volume, min(h[l], h[r]) * (r-l))

        return volume
