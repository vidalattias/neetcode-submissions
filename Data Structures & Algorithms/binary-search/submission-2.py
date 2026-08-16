class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def aux(i, j):
            print(f"{i} - {j}")
            if i > j:
                return -1
            if i == j:
                return i if nums[i] == target else -1

            mid = i + (j-i+1)//2
            vm = nums[mid]
            if vm == target:
                return mid
            elif vm > target:
                # explore left
                new_i = i
                new_j = mid - 1
                return aux(new_i, new_j)
            else:
                # explore right
                new_i = mid + 1
                new_j = j
                return aux(new_i, new_j)

        return aux(0, len(nums)-1)