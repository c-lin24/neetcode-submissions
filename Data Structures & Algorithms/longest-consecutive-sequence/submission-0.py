class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        cnt = 0
        for x in s: 
            if x-1 not in s: 
                y = x
                while y in s: 
                    y += 1

                cnt = max(y-x, cnt)

        return cnt

