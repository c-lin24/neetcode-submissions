class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = []
        
        for i in range(len(nums) - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue

            fixed = sorted_nums[i]
            l = i+1
            r = len(sorted_nums)-1

            while l < r: 
                s = fixed + sorted_nums[l] + sorted_nums[r]
                if s == 0: 
                    result.append([sorted_nums[l], sorted_nums[r], fixed])
                    l += 1
                    r -= 1
                    while l < r and sorted_nums[l] == sorted_nums[l-1]:
                        l += 1
                    while l < r and sorted_nums[r] == sorted_nums[r+1]:
                        r -= 1

                elif s < 0: 
                    l += 1
                else: 
                    r -= 1

        return result

