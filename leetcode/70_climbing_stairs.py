class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0 for _ in range(n)]
        dp[0] = 1
        dp[1] = 2

        for i in range(2, len(dp)):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n - 1]