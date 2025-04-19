class Node:
    def __init__(self):
        self.child = {}
        self.endOfWord = False
class Trie:
    def __init__(self) -> None:
        self.root = Node()
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.child:
                cur.child[c] = Node()
            cur = cur.child[c]
        cur.endOfWord = True
    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.child:
                return  False
            cur = cur.child[c]
        return cur.endOfWord
    def startWith(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.child:
                return False
            cur = cur.child[c]
        return True