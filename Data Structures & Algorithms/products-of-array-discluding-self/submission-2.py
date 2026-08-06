class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        pre_run = 1
        suf_run = 1
        n = len(nums)

        #prefix
        for i in range(n):
            if i == 0:
                prefix.append(1)
            else: 
                pre_run *= nums[i-1]
                prefix.append(pre_run)

        for i in range(n - 1, -1, -1):
            if i == len(nums) - 1: 
                suffix.append(1)
            else: 
                suf_run *= nums[i+1]
                suffix.append(suf_run)

        for i in range(n):
            prefix[i] *= suffix[n-i-1]   

        return prefix     