class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp[x] means the length of LIS until x
        n = len(nums)
        dp = [1] * (n)

        for i in range(1, n):
            curr_max = 0
            for j in range(i):
                if nums[j] < nums[i]: 
                    curr_max = max(dp[j], curr_max)
            dp[i] = curr_max + 1 

        return max(dp)

