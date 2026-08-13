class Solution:
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()

        ret = []
        for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1,N):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        if tmp not in ret:
                            ret.append(tmp)
        return ret

    def threeSum(self, nums):
        nums.sort()
        N = len(nums)
        res = []

        for i in range(N-2):
            v = nums[i]
            l = i+1
            r = N-1

            while l < r:
                trio = v + nums[l] + nums[r]
                ilr = [v, nums[l], nums[r]]
                if trio < 0:
                    l += 1
                elif trio > 0:
                    r -= 1
                else:
                    if ilr not in res:
                        res.append(ilr)
                    l += 1
                    r -= 1
        return res