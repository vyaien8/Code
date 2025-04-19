class Solution:
    def solve(self, board: [[str]]):
        row, col = len(board), len(board[0])
        d = [[1,  0], [-1, 0], [0, 1], [0, -1]] 
        def dfs(r, c):
            board[r][c] = '*'
            for dr, dc in d:
                nrow, ncol = r + dr, c + dc
                if nrow in range(row) and ncol in range(col) and board[nrow][ncol] == 'O':
                    dfs(nrow, ncol)
        for r in range(row):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][col - 1] == 'O':
                dfs(r, col - 1)
        for c in range(col):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[row - 1][c] == 'O':
                dfs(row - 1, c)
        for r in range(row):
            for c in range(col):
                if board[r][c] == '*':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'
test = Solution()
test.solve([["O","O","O"],["O","O","O"],["O","O","O"]])