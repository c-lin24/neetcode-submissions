class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, value in enumerate(nums):
            compl = target - value
            if compl in seen: 
                return [seen[compl], i]

            seen[value] = i