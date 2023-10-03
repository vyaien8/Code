class Solution:
    def dailyTemperatures(self, temp):
        res = [0] * len(temp)
        stack = []
        for i in range(len(temp)):
            # if stack is not empty and temp[i] > temp[stack.top()]
            # -> meet the day warmer
            while stack and temp[i] > temp[stack[-1]]: 
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res
