class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        N = len(nums)

        prod = 1
        for n in nums:
            if n == 0:
                zero_count += 1
            else:
                prod *= n

        if zero_count > 1:
            return [0]*N
        
        if zero_count == 1:
            return [prod if n == 0 else 0 for n in nums]

        return [prod//n for n in nums]