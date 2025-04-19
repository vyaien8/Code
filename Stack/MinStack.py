class MinStack:
    def __init__(self):
        self.mStack = []
        self.stack = []
    def push(self, val):
        if self.mStack == [] or self.mStack[-1] > val:
            self.mStack.append(val)
        self.stack.append(val)
    def pop(self):
        if self.stack[-1] == self.mStack[-1]:
            self.mStack.pop()
        self.stack.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.mStack[-1]
