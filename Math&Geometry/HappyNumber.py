class Solution:
    def isHappy(self, n: int):
        def sumSquare(n):
            res = 0
            while n:
                res += (n%10) ** 2
                n //= 10
            return res
        cycle = set()
        while n not in cycle:
            cycle.add(n)
            n = sumSquare(n)
            if n == 1:
                return True
        return False
    def floyd(self, n: int):
        def sumSquare(n):
            res = 0
            while n:
                res += (n%10) ** 2
                n //= 10
            return res
        slow, fast = n, sumSquare(n)
        while slow != fast:
            fast = sumSquare(sumSquare(fast))
            slow = sumSquare(slow)
        return slow == 1
             
test = Solution()
print(test.isHappy(19))