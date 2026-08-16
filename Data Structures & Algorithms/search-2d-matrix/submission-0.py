class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def find_in_row(i, j, row):
            values = matrix[row]
            if i > j:
                return False
            if i == j:
                return True if values[i] == target else False

            mid = i + (j-i+1)//2
            val_mid = values[mid]
            if val_mid == target:
                return True
            elif val_mid < target:
                # explore right
                new_i = mid + 1
                new_j = j
            else:
                # explore left
                new_i = i
                new_j = mid - 1

            return find_in_row(new_i, new_j, row)

        def find_row(i, j):
            print(f'Find row {i} - {j}')
            if i > j:
                return False
            if i == j:
                min_val = matrix[i][0]
                max_val = matrix[i][-1]
                if min_val <= target <= max_val:
                    return find_in_row(0, len(matrix[i])-1, i)
                else:
                    return False
                
            mid_index = i + (j-i+1)//2
            mid_min = matrix[mid_index][0]
            mid_max = matrix[mid_index][-1]

            if mid_min <= target <= mid_max:
                return find_in_row(0, len(matrix[mid_index])-1, mid_index)
            elif target < mid_min:
                # explore left
                new_i = i
                new_j = mid_index - 1
                return find_row(new_i, new_j)
            else:
                # explore right
                new_i = mid_index + 1
                new_j = j
                return find_row(new_i, new_j)

        return find_row(0, len(matrix)-1)
            