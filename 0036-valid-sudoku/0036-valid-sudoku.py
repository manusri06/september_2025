class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[] for i in range(9)]
        col = [[] for i in range(9)]
        box = [[] for i in range(9)]
        for i in range(9):
            for j in range(9):
                n = board[i][j]
                bi = (i//3)*3+(j//3)
                if n == ".":
                    continue
                if n in row[i] or n in col[j] or n in box[bi]:
                    return False
                row[i].append(n)
                col[j].append(n)
                box[bi].append(n)
        return True
