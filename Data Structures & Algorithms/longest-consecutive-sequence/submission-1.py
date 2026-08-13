class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        if nums == []:
            return 0

        current = 1
        best = 1

        for i, n in enumerate(nums):
            if nums[i-1] == n:
                continue
            elif nums[i-1] == n-1:
                current += 1
                best = max(best, current)
            else:
                current = 1
        return best