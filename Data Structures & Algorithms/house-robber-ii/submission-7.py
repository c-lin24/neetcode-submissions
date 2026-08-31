class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        return max(self.solve(nums[1:]), self.solve(nums[:-1]))


    def solve(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        maxs = [0] * len(nums)
        maxs[0] = nums[0]
        maxs[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            maxs[i] = max(maxs[i-2] + nums[i], maxs[i-1])

        return maxs[-1]