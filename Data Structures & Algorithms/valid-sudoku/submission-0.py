class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[[0]*9 for _ in range(9)]
        col=[[0]*9 for _ in range(9)]
        boxes=[[0]*9 for _ in range(9)]
##TC=O(n^2) and SP=O(n^2)

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                val=int(board[r][c])-1
                
                if rows[r][val]==1:
                    return False
                rows[r][val] =1

                if col[c][val]==1:
                    return False
                col[c][val]=1

                boxIdx=3*(r//3)+(c//3)

                if boxes[boxIdx][val]==1:
                    return False
                boxes[boxIdx][val]=1
        return True
