from collections import deque
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: [str]):
        if endWord not in wordList:
            return 0
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j + 1:]
                nei[pattern].append(word)
        visit = set()
        q = deque()
        visit.add(beginWord)
        q.append(beginWord)
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j + 1:]
                    for n in nei[pattern]:
                        if n not in visit:
                            q.append(n)
                            visit.add(n) 
            res += 1
        return 0