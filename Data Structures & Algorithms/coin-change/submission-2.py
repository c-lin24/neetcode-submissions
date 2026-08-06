class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #dp[x] = min coins to make sum x
        if amount == 0: 
            return 0

        if not coins: 
            return -1

        #larger than ANY possible answer
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for x in range(1, amount + 1):
            for c in coins: #consider c as last coin to be used
                if 0 <= x - c:
                    dp[x] = min(dp[x], dp[x-c] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1        
