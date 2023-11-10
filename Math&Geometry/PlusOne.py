class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        carry = 0
        digits[-1] += 1
        if digits[-1] >= 10:
            digits[-1] -= 10
            carry = 1
        for i in range(len(digits) - 2, -1, -1):
            digits[i] += carry
            carry = 0
            if digits[i] >= 10:
                digits[i] -= 10
                carry = 1
        return [1] + digits if carry else digits