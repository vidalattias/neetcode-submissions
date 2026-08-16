class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def aux(i, j):
            if i > j:
                return -1
            if i == j:
                return i if nums[i] == target else -1

            mid = i + (j-i+1)//2
            value_mid = nums[mid]

            if value_mid == target:
                return mid
            elif value_mid < target:
                # explore right
                new_i = mid + 1
                new_j = j
            else:
                # explore left
                new_i = i
                new_j = mid - 1
            return aux(new_i, new_j)
        return aux(0, len(nums)-1)