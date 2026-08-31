class Solution:
    def numSquares(self, n: int) -> int:
        
        mins = [n] * (n+1)  #mins[i] is the least number of perf square required to sum to i

        mins[0] = 0
        
        for i in range(1, n+1):
            if (isinstance(math.sqrt(i), int)):
                mins[i] = 1 

            for j in range(1, math.floor(math.sqrt(i)) + 1):
                mins[i] = min(mins[i], mins[i-j**2] + 1)

        return mins[n]