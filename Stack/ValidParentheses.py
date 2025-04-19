class Solution:
    def isValid(self, s):
        m = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c in m: # when closing parenthese coming
                if stack and stack[-1] == m[c]: # the last element of current stack must be the correct open parenthese
                   stack.pop()
                else: 
                    return False
            else: # when it is open parenthese
                stack.append(c)
        return not stack