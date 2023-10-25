class Solution:
    # brute forcing
    def exist(self, board: [[str]], word: str) -> bool:
        start = []
        n = len(board)
        m = len(board[0])
        k = len(word)
        # find the first letter
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    start.append((i,j))
        if not start:
            return False
        res = []
        # find the remain
        def search(i, j, cur, c):
            if c == k:
                res.append(cur[:])
                return
            if i + 1 < n and j < m and (i+1, j) not in cur and board[i + 1][j] == word[c]:
                cur.append((i+1, j))
                search(i + 1, j, cur, c + 1)
                cur.pop()
            if i < n and j + 1 < m and (i, j+1) not in cur and board[i][j + 1] == word[c]:
                cur.append((i, j+1))
                search(i, j + 1, cur, c + 1)
                cur.pop()
            if i - 1 >= 0 and j < m and (i - 1, j) not in cur and board[i - 1][j] == word[c]:
                cur.append((i - 1, j))
                search(i - 1, j, cur, c + 1)
                cur.pop()
            if i < n and j - 1 >= 0 and (i, j-1) not in cur and board[i][j - 1] == word[c]:
                cur.append((i, j-1))
                search(i, j - 1, cur, c + 1)
                cur.pop()

        for i, j in start:
            search(i,j,[(i,j)],1)
            if res:
                return True
        return False
    
    def exist(self, board: [[str]], word: str) -> bool:
        n, m, k  = len(board), len(board[0]), len(word)
        path = set() 
        def bk(i, j, c):
            if c == k:
                return True
            if i < 0 or j < 0 or i >= n or j >= m or board[i][j] != word[c] or (i, j) in path:
                return False
            path.add((i, j))
            res = bk(i + 1, j, c + 1) or bk(i - 1, j, c + 1) or bk(i, j + 1, c + 1) or bk(i, j - 1, c + 1)
            path.remove((i,j))
            return res
        for i in range(n):
            for j in range(m):
                if bk(i, j, 0):
                    return True
        return False
 

            
        

        

        