class Solution:
    def genParentheses(self, n):
        res = []
        stack = []
        def bk(o, c):
            if c == n: # if closing equal n
                res.append(''.join(stack))
                return
            if o < n: # if open less than n 
                stack.append("(")
                bk(o + 1, c)
                stack.pop()
            if c < o: # if closing less than open
                stack.append(")")
                bk(o, c + 1)
                stack.pop()
        bk(0, 0)
        return res
                

