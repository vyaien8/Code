class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        i, j = 0, len(s) - 1
        while i < j:
            if s[i].isalnum() == False:
                i += 1
                continue
            elif s[j].isalnum() == False:
                j -= 1
                continue
            else:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
        return True