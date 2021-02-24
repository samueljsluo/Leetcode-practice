class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # abcdae
        # acae
        # if last char is same(e), the last LCS come from [i-1][j-1](a)
        # abc
        # ace
        # if last char is not same, the last LCS come from either [i-1][j] or [i][j-1] depend on which one is larger.
        # since max one is current max LCS
        text1 = '#' + text1
        text2 = '#' + text2
        m = len(text1)
        n = len(text2)
        dp = [[0]*n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
        