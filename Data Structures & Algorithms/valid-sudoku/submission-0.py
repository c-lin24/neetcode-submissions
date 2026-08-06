class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            hs = set()

            for j in range(9):
                cur = board[i][j]
                if cur != "." and cur in hs:
                    return False
                else:
                    hs.add(cur)
        
        for i in range(9):
            hs = set()

            for j in range(9):
                cur = board[j][i]
                if cur != "." and cur in hs:
                    return False
                else:
                    hs.add(cur)

        for box in range(9):
            hs = set()
            
            start_row = (box // 3) * 3
            start_col = (box % 3) * 3

            for i in range(3):
                for j in range(3):
                    cur = board[start_row + i][start_col + j]

                    if cur != ".":
                        if cur in hs:
                            return False
                        hs.add(cur)

        return True

        
