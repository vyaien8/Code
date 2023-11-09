class Solution:
    def reverse(self, x: int):
        res = 0
        sign = 1
        if x < 0:
            sign = -1
            x *= -1
        while x:
            res *= 10
            res += x % 10
            x //= 10
        res *= sign
        return res if res >= -2147483648 and res <= 2147483647 else 0
test = Solution()
print(test.reverse(-123))