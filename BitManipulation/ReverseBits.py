class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res *= 2
            res += n % 2
            n >>= 1
        return res