class Solution:
    def solveNQueens(self, n: int) -> [[str]]:
        col = set()
        posDiag = set() # every position on the same positive diag has the same r + c
        negDiag = set() # every position on the same negative diag has the same r - c
        res = []
        board = [["."] * n for i in range(n)]
        # for each row only one Q
        def bk(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = 'Q'
                bk(r+1)
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = '.'
        bk(0)
        return res
            
