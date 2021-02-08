class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # backtracking, O(n*2^n) since there would be 2^n possible substring in the worst case
        temp = []
        res = []
        self.backtracking(s, res, temp, 0)
        return res
    
    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
        
    def backtracking(self, s, res, temp, start):
        if start >= len(s):
            res.append(temp[:])
            return
        for end in range(start, len(s)):
            if self.isPalindrome(s, start, end):
                temp.append(s[start:end+1])
                self.backtracking(s, res, temp, end+1)
                temp.pop()


        # backtracking with DP
#         n = len(s)
#         dp = [[0 for i in range(n)] for j in range(n)]
#         res = []
#         self.dfs(res, s, 0, [], dp)
#         return res
        
#     def dfs(self, res, s, start, temp, dp):
#         if start >= len(s):
#             res.append(temp[:])
#             return
        
#         for end in range(start, len(s)):
#             if s[end] == s[start] and (end-start <= 2 or dp[start+1][end-1]):
#                 dp[start][end] = True
#                 temp.append(s[start:end+1])
#                 self.dfs(res, s, end+1, temp, dp)
#                 temp.pop()
