class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            
            cur = 1
            for direc in [[1,0], [0,1], [-1,0], [0,-1]]:
                cur += dfs(r + direc[0], c + direc[1]) 

            return cur

        maxi = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = dfs(r, c)
                maxi = max(maxi, area)

        return maxi
