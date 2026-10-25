class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [0] * (n + 1)  # We create a table consisted of 0 to the number of steps + 1
        dp[1] = 1  # To reach 1st stair take 1 step
        dp[2] = 2  # To reach 2nd stair take 2 steps

        # From the third stair to the number of steps + 1, we fill the
        for i in range(3, n + 1):
            """Every step going forward from 3rd stair will use
            the summation of previous two stair's steps"""
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]  # Return the computed result of the given step from our dp table
