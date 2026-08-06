class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:                    
        def dfs(r, c, visited):
            if (r, c) in visited: 
                return 
            visited.add((r, c)) #use tuples instead, not lists, as tuples is hashable

            for pair in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                new_r = r + pair[0]
                new_c = c + pair[1]
                if 0 <= new_r < len(heights) and 0 <= new_c < len(heights[0]) and heights[new_r][new_c] >= heights[r][c] :
                    dfs(new_r, new_c, visited)
        
            return visited

        r_cap = len(heights)
        c_cap = len(heights[0])
        res = []
        pacific = set()
        atlantic = set()

        for i in range(r_cap):
            for j in range(c_cap):
                if i == 0 or j == 0:
                    dfs(i, j, pacific)
                
                if i == r_cap - 1 or j == c_cap - 1:
                    dfs(i, j, atlantic)

        res = [list(cell) for cell in atlantic & pacific]

        return res
