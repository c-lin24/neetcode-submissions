class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        maxs = [0] * n # maxs[i] is the max robbed at ith house

        if n < 2:
            return nums[0]

        maxs[0] = nums[0]
        maxs[1] = max(nums[0], nums[1]);

        for i in range(2, n):
            maxs[i] = max(maxs[i-2] + nums[i], maxs[i-1])

        return maxs[n-1]
        