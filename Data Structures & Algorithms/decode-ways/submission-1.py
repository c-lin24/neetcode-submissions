class Solution:
    def numDecodings(self, s: str) -> int:
        
        #dp[i] is the number of ways to decode substring from [i..n]
        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1

        for i in range(n-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
                continue

            #for single digit
            dp[i] = dp[i+1]

            #if the double digit with i+2 is valid, then add all ways from i+2, skipping i+1
            if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456')):
                dp[i] += dp[i+2]

        return dp[0]
                
            

        