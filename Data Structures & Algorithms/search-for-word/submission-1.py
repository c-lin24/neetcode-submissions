class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        path = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                (r,c) in path or word[i] != board[r][c]):
                return False

            path.add((r,c))
            acc = False
            for dr, dc in [[1,0], [0,1], [-1,0], [0,-1]]:
                acc = acc or dfs(r + dr, c + dc, i + 1)
            
            path.remove((r,c))
            return acc 
                
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False