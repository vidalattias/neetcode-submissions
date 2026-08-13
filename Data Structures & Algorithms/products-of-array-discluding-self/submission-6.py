class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        l2r = [1]
        for i in range(1,N):
            l2r.append(nums[i-1] * l2r[-1])

        r2l = [1]*N
        for i in range(N-2,-1, -1):
            val = r2l[i+1] * nums[i+1]
            r2l[i] = val

        outputs = [l2r[i]*r2l[i] for i in range(N)]
        return outputs