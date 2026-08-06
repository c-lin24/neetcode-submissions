class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}  #coord to number fo ways
        
        for i in range(1, m+1): 
            memo[(i, 1)] = 1

        for j in range(1, n+1):
            memo[(1, j)] = 1


        def dfs(m, n): 
            if (m, n) in memo: 
                return memo[(m, n)]

            if m - 1 > 0 and n - 1 > 0:
                memo[(m, n)] = dfs(m - 1, n) + dfs(m, n - 1)

            return memo[(m, n)]

        return dfs(m, n)

        

