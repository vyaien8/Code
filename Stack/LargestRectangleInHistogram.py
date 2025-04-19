class Solution:
    def largestRectArea(self, heights):
        stack = []
        res = -1
        i = 0
        while i < len(heights):
            if not stack or heights[i] >= heights[stack[-1]]: #if stack is empty or can expend to the right
                stack.append(i)
                i += 1
            else:
                index = stack[-1]
                stack.pop()
                if not stack: # if stack is empty, that mean no 
                    res = max(res, heights[index] * i)
                else:
                    res = max(res, heights[index] * (i - 1 - stack[-1]))
        while stack:
            index = stack[-1]
            stack.pop()
            if not stack:
                res = max(res, heights[index] * i)
            else:
                res = max(res, heights[index] * (i - stack[-1] - 1))
        return res
    
    def largestRectangleArea(self, heights):
        res = 0
        st = [] # pair(index, height)
        for i,h in enumerate(heights):
            start = i
            while st and st[-1][1] > h: # if current height is less than top of stack
                # mean that no longer append to the right
                index, height = st.pop()
                res = max(res, height * (i - index))
                start = index # store the left most appendable index
            st.append(start, h)
        for i, h in st: # the rest of stack, always can append to the end of stack
            res = max(res, h * (len(height) - i))
        return res

