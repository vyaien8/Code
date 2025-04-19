class Solution:
    def mutiply(self, num1: str, num2: str):
        if '0' in [num1, num2]:
            return '0'
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = (ord(num1[i1]) - 0x30) * (ord(num2[i2]) - 0x30)
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += (res[i1 + i2] // 10) # carry
                res[i1 + i2] %= 10
        res, b = res[::-1], 0
        while b < len(res) and res[b] == 0:
            beg += 1
        res = map(str, res[b:])
        return ''.join(res)
