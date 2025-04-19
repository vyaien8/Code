class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # max frequent can be is len(nums)

        for i in nums:
            count[i] = 1 +count.get(i, 0)
        for i, c in count.items():
            freq[c].append(i) # list element has frequent c
        res = []
        for i in range(len(freq) - 1, 0, -1): # search from hight frequent down
            for e in freq[i]: 
                res.append(e)
                if len(res) == k:
                    return res