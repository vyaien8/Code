class Solution:
    def carFleet(self, target, position, speed):
        stack = [] # number car left in stack is fleet car
        pair = [[p, s] for p, s in zip(position, speed)]
        for p, s in sorted(pair)[::-1]:
            t = (target - p) / s
            if not stack or t > stack[-1]: # if car not in stack or its time to reach target bigger than the last one on stack 
                stack.append(t)
        return len(stack)

            