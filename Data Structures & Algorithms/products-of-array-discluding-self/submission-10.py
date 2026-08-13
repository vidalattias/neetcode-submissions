class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        zero_index = None
        N = len(nums)
        for i,n in enumerate(nums):
            if n == 0:
                zero_count += 1
                zero_index = i

        if zero_count > 1:
            return [0]*N
        
        if zero_count == 1:
            term = 1
            for n in nums:
                if n!=0:
                    term *= n
            return [term if i == zero_index else 0 for i in range(N)]

        total = 1
        for n in nums:
            total *= n

        return [total//n for n in nums]