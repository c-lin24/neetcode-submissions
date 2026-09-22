class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        lo = 0
        hi = n * m - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            val = matrix[mid // m][mid % m]

            if val == target: 
                return True
            elif val < target: 
                lo = mid + 1
            else: 
                hi = mid -1
                
        return False

        