class Solution:
    def climbStairs(self, n: int) -> int:
        # initialize dp array and add dp[0] and dp[1] as 1, because there is only 1 possible solution for this.
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1

        if n == 0 or n==1:
            return 1

        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]

        return dp[n]