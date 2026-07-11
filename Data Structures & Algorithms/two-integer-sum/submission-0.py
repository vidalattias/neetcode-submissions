class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t_i = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in t_i:
                return [t_i[diff], i]
            t_i[nums[i]] = i