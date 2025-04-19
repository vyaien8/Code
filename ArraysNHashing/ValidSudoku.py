class Solution:
    def isValidSudoku(self, board):
        cols = {}
        rows = {}
        squares = {}
        for r in range(9):
            rows[r] = [] # create dictionary
            for c in range(9):
                if c not in cols: # create dictionary
                    cols[c] = []
                if (r//3, c//3) not in squares:
                    squares[(r //3, c//3)] = []
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r //3, c//3)]:
                    return False
                cols[c].append(board[r][c])
                rows[r].append(board[r][c])
                squares[(r //3, c//3)].append(board[r][c])
        return True        
        