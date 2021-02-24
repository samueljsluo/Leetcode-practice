class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP
        # time complexity: O(amount * len(coins))
        # space complexity: O(amount)
        # coins [1,2,5]
        # amount 11
        #     dp[0] dp[1] dp[2] dp[3] dp[4] dp[5] dp[6] dp[7] dp[8] dp[9] dp[10] dp[11]
        #  1    0     1     2     3     4     5     6     7     8     9     10     11
        #  2    0     1     1     2     2     3     3     4     4     5      5      6
        #  5    0     1     1     2     2     1     2     2     3     3      2      3
        dp = [0] + [float('inf')] * (amount)
        for c in coins:
            for i in range(c, amount+1):
                dp[i] = min(dp[i], dp[i-c] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
            