class Solution:
    def numDecodings(self, s: str) -> int:
        # Solution 1: Recursive with mem
        # s-num of solutions
        # basically is check 1 and 2 prefix are valid and solve the sub-problem of s[1:] and s[2:]
        #      1026-2
        #      /  \
        #   026-0 26-2
        #        /  \
        #       6-1 ''-1
#         if len(s) == 0: return 0
#         mem = defaultdict(int)
#         mem[''] = 1
#         self.helper(s, mem)
#         return mem[s]
        
#     def helper(self, s, mem):
#         if s in mem: return mem[s]
#         if s[0] == '0': return 0
#         if len(s) == 1: 
#             mem[s] = 1
#             return 1
#         w = self.helper(s[1:], mem)
#         prefix = int(s[:2])
#         if prefix <= 26:
#             w+=self.helper(s[2:], mem)
#         mem[s] = w
#         return w

        # Solution 2: DP
        # 4 sitsuations
        # s[i] and s[i-1]s[i] not valid, dp[i]=0
        # s[i] valid, dp[i]+=dp[i-1]
        # s[i-1]s[i] valid, dp[i]+=dp[i-2]
        # s[i] and s[i-1]s[i] valid, dp[i] = dp[i-1] + dp[i-2]
        # 1026
        #   i     s[i]    s[i-1]s[i]  dp
        #  -1      NA          NA     1
        #   0      1           NA     1
        #   1      0x          10     1
        #   2      2           02x    1
        #   3      6           26     2
        
        # if len(s) == 0: return 0
        # if s[0] == '0': return 0
        # dp1 = 1 # i-1
        # dp2 = 1 # i-2
        # for i in range(1, len(s)):
        #     dp = 0
        #     if int(s[i]) == 0 and int(s[i-1] + s[i]) > 26: dp = 0
        #     if int(s[i]) > 0: dp = dp1
        #     if 9 < int(s[i-1]+s[i]) <= 26: dp+=dp2
        #     dp2 = dp1
        #     dp1 = dp
        # return dp1
        
        if len(s) == 0: return 0
        if s[0] == '0': return 0
        dp = [0]*(len(s)+1)
        dp[0], dp[1] = 1, 1
        for i in range(1, len(s)):
            if int(s[i]) == 0 and int(s[i-1] + s[i]) > 26: dp[i] = 0
            if int(s[i]) > 0: dp[i+1] = dp[i] 
            if 9 < int(s[i-1]+s[i]) <= 26:
                dp[i+1]+=dp[i-1]
        return dp[-1]
            
                