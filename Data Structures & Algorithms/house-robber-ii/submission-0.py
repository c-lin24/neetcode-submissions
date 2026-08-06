class Solution:
    def rob(self, nums: List[int]) -> int:
        #either 0 to n-2 OR 1 to n-1

        def rob_linear(a):
            prev2, prev1 = 0, 0

            for x in a:
                tmp = prev1
                prev1 = max(prev1, prev2 + x)
                prev2 = tmp
                
            return prev1
        
        if len(nums) == 1: return nums[0]
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))