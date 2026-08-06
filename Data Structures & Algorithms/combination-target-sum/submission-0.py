class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur_comb, total):
            if total == target:
                res.append(cur_comb.copy())
                return
            
            elif i >= len(nums) or total > target: 
                return
            
            cur_comb.append(nums[i])
            dfs(i, cur_comb, total + nums[i]) #add the current candidate again
            cur_comb.pop()
            dfs(i + 1, cur_comb, total) #try the next value
        
        dfs(0, [], 0)
        return res
            


            
