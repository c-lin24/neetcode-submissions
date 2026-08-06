class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        l = 0
        r = ROWS * COLS - 1

        while l <= r:
            mid = (l + r) // 2
            m = mid // COLS  #matrix[m][n]
            n = mid % COLS
            if matrix[m][n] == target:
                return True
            elif matrix[m][n] < target: 
                l = mid + 1
            else:
                r = mid - 1

        return False
            