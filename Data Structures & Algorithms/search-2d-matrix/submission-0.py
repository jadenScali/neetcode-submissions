import math

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)

        if m == 0:
            return False

        n = len(matrix[0])

        l = 0
        r = m*n - 1

        while l <= r:
            mid = math.floor((l + r) / 2)
            val = matrix[math.floor(mid/n)][mid%n]

            if target == val:
                return True
            elif target < val:
                r = mid - 1
            else:
                l = mid + 1
            
        
        return False
