class Node:
    def __init__(self):
        self.child = {}
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.child:
                cur.child[c] = Node()
            cur = cur.child[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(i, root: Node):
            cur = root
            for j in range(i, len(word)):
                c = word[i]
                if c == ".":
                    for ch in cur.child.values():
                        if dfs(j + 1, ch):
                            return True
                    return False
                else:
                    if c not in cur.child:
                        return False
                    cur = cur.child[c]
            return cur.endOfWord
        return dfs(0, self.root)
        




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)