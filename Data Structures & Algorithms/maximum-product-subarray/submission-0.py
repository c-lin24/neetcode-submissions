class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #min_end[i]: keep track of both the max and min ending at i
        n = len(nums)
        min_end= [0] * n
        max_end= [0] * n
        min_end[0] = nums[0]
        max_end[0] = nums[0]
        ans = nums[0]

        for i in range(1, n):
            max_end[i] = max(nums[i], nums[i]*max_end[i-1], nums[i]*min_end[i-1])
            min_end[i] = min(nums[i], nums[i]*max_end[i-1], nums[i]*min_end[i-1])
            ans = max(ans, max_end[i])
            
        return ans