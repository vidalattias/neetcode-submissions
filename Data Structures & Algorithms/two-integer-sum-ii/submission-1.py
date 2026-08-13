class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = {}
        for i, n in enumerate(numbers):
            if n in s:
                return [s[n]+1, i+1]
            else:
                diff = target - n
                s[diff] = i
