class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = ""
        longest_len = 0
        for i in range(n):
            l, u = 0, 0
            
            l = i
            u = i 
            while l >= 0 and u < n and s[u] == s[l]:
                u += 1
                l -= 1
            if u-l-1 > longest_len: 
                longest = s[l+1:u]
                longest_len = u - l - 1
            

            l = i
            u = i + 1
            while l >= 0 and u < n and s[u] == s[l]:
                l -= 1
                u += 1


            if u - l - 1 > longest_len:
                longest = s[l+1:u]
                longest_len = u - l - 1
    
        return longest  
                