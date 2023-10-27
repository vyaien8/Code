class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        prev = 1
        cur = 2
        for i in range(3, n + 1):
            prev, cur = cur, cur + prev
        return cur
        