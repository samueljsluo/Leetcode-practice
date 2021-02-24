class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Solution 1:
        # Recursive with memory
        # isWord(left) && isWord(right)
        # use a mem to store result to avoid double check
        # s = applepen
        # split index is 5
        # if apple in dict and pen is also in dict --> return true
#         mem = defaultdict(bool)
#         return self.helper(s, wordDict, mem)
        
#     def helper(self, s, wordDict, mem):
#         if s in mem:
#             return mem[s]
#         if s in wordDict:
#             mem[s] = True
#             return True
#         for i in range(1, len(s)):
#             left = s[0:i]
#             right = s[i:]
#             if left in wordDict and self.helper(right, wordDict, mem):
#                 mem[s] = True
#                 return True
#         mem[s] = False
#         return False

        # Solution 2:
        # DP
        # if previous s[j] is in dict and s[j:i] is also in dict
        # applepenapple
        # [apple, pen]
        # applepenapple
        #|----|---|---|
        #j    i
        # if j is true and s[j:i] in dict --> dp[i] = true
        # applepenapple
        #|----|---|---|
        #     j   i
        # dp[j] is true and we found that s[j:i] in dict --> dp[i] = true
        wordDict = set(wordDict)
        dp = [False]*(len(s)+1)
        dp[0] = True  # have to set to True, otherwise can't find any word
        
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]