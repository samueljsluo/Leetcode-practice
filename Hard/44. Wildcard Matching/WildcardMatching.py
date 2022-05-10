class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        
        s = '#' + s
        p = '#' + p
        
        dp = [[False for _ in range(n+1)] for i in range(m+1)]
        dp[0][0] = True
        
        # dp[0][j] edge case
        for j in range(1, n+1):
            if p[j] != '*':
                break
            dp[0][j] = True
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                elif p[j] == s[i]:
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]