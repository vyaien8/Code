class Solution:
    def mergeTriplets(self, triplets: [[int]], target: [int]) -> bool:
        res = [0,0,0]
        for t in triplets:
            for i in range(3):
                if t[i] > target[i]:
                    i -= 1
                    break
            if i == 2:
                for i in range(3):
                    res[i] = max(res[i], t[i])
                if res == target:
                    return True
        return False
        

