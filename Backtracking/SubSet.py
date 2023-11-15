class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        res = []
        subset = []
        #0                        []
        #1            [1]                         []
        #2    [1, 2]          [1]            [2]        []
        #3[1, 2, 3] [1, 2]  [1, 3] [1]     [2, 3] [2]  [3]  []
        def dfs(i):
            if i == len(nums): # reach the leaf node of tree
                res.append(subset.copy())
                return

            subset.append(nums[i]) # add it
            dfs(i + 1)
            subset.pop() # backtrack to go into not add it
            dfs(i + 1)
        dfs(0)
        return res
