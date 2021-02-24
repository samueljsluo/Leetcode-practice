class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Solution 1: Recursive with mem, top-down
#         mem = [[-1 for i in range(n+1)] for j in range(m+1)]
#         return self.path(m, n, mem)
    
#     def path(self, m, n, mem):
#         if m < 1 or n < 1: return 0
#         if m==1 and n==1: return 1
#         if mem[m][n] > 0: return mem[m][n]
#         mem[m][n] = self.path(m-1, n, mem) + self.path(m, n-1, mem)
#         return mem[m][n]

        # Solution 2: DP, bottom-up
        dp = [[0 for i in range(n+1)] for j in range(m+1)] # n+1 and m+1 for edge case
        dp[1][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i==1 and j==1: continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]