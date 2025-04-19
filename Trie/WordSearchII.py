class Trie:
    def __init__(self) -> None:
        self.children = {}
        self.isWord = False
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur[c] = Trie()
            cur = cur[c]
        cur.isWord = True
class Solution:
    def findWords(self, board: [[str]], words: [str]):
        root = Trie()
        for w in words:
            root.addWord(w)
        R, C = len(board), len(board[0])
        res, visit = set(), set()
        def bk(r: int, c: int, node: Trie, word: str):
            if r < 0 or c < 0 or r >= R or c >= C or (r, c) in visit or board[r][c] not in node.children:
                return
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            bk(r + 1, c, node, word)
            bk(r - 1, c, node, word)
            bk(r, c + 1, node, word)
            bk(r, c - 1, node, word)
            visit.remove((r,c))

        for r in range(R):
            for c in range(C):
                bk(r,c,root,'')
        return list(res)