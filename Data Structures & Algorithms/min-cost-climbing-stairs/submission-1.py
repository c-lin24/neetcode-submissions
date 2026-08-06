class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        mi = [0] * n
        mi[0] = cost[0]
        mi[1] = cost[1]

        for i in range(2, n):
            mi[i] = cost[i] + min( mi[i-1], mi[i-2])

        return min(mi[n-1], mi[n-2])
        
