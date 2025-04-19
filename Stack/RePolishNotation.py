class Solution:
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i == "+":
                tmp = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(tmp)
            elif i == "-":
                tmp = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(tmp)
            elif i == "*":
                tmp = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(tmp)
            elif i == "/":
                tmp = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(tmp)
            else:
                stack.append(int(i))
        return stack[-1]
