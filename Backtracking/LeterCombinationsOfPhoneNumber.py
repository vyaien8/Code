class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        if not digits:
            return []
        res = []
        d = {"2": ["a", "b", "c"],
             "3": ["d", "e", "f"],
             "4": ["g", "h", "i"],
             "5": ["j", "k", "l"],
             "6": ["m", "n", "o"],
             "7": ["p", "q", "r", "s"],
             "8": ["t", "u", "v"],
             "9": ["w", "x", "y", "z"]}
        cur = []
        def bk(i):
            if i >= len(digits):
                res.append(''.join(cur))
                return
            for c in d[digits[i]]:
                cur.append(c)
                bk(i + 1)
                cur.pop()
        bk(0)
        return res

test = Solution()
print(test.letterCombinations("23"))

