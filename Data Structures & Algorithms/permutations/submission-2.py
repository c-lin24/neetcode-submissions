class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:]) # must append a copy rather than the actual list
                return

            for i, x in enumerate(nums):
                if used[i]:
                    continue
                
                used[i] = True   # keep track of what has already been picked, so can be avoided
                path.append(x)
                backtrack()
                path.pop()
                used[i] = False

        backtrack()
        return res