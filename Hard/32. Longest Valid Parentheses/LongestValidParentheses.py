class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Solution 1: brute force
        def brute_force(s):
            def isValid(x):
                stack = []
                for i in range(len(x)):
                    if x[i] == '(':
                        stack.append('(')
                    elif stack!=[] and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                return len(stack)==0
            if len(s) == 0 or len(s) == 1:
                return 0
            n = len(s)
            for i in range(n if n % 2 == 0 else n-1, 0, -2): # each two char
                for j in range(n-i+1): # next candidate
                    if isValid(s[j:j+i]):
                        return i
            return 0
        
        # Solution 2: DP
        def DP(s):
            if len(s) < 2:
                return 0
            dp = [0] * len(s)
            for i in range(1, len(s)):
                # dp[i-1] is previous valid parentheses
                # i-dp[i-1]-1 chech if there is a corresponding '(' at this position
                # So dp transform func is 2(valid) + 
                #                         dp[i-1] valid which include in current () + 
                #                         dp[i - dp[i-1] - 2] consecutive
                # i ()())
                # 0 00000
                # 1 02000 2 + 0 + 0
                # 2 02000
                # 3 02040 2 + 0 + 2
                # 4 02040
                if s[i] == ')' and \
                i - dp[i - 1] - 1 >= 0 and \
                s[i - dp[i - 1] - 1] == '(':  
                    # check there is valid parentheses
                    # ())( prevent this case
                    dp[i] = 2 + dp[i-1] + dp[i - dp[i-1] - 2]
            return max(dp)
    
        # Solution 3: stack
        def stack(s):
            stk = [-1] # default
            length = 0
            max_len = 0
            for i in range(len(s)):
                if s[i] == '(':
                    stk.append(i) # store index
                else:
                    stk.pop()
                    if len(stk) == 0: # there is a invalid parenthese
                        # so start from this point to find next valid one
                        stk.append(i) 
                        continue
                    length = i - stk[-1]
                    max_len = max(max_len, length)
                if len(stk) == 0:
                    length = 0
            return max_len
        
        def solution4(s):
            left = 0
            right = 0
            max_len = 0
            # left to right
            for i in range(len(s)):
                if s[i] == '(':
                    left+=1
                else:
                    right+=1
                if left == right: # valid paratheses
                    max_len = max(max_len, left * 2)
                if right > left: # invalid point
                    left, right = 0, 0
                    
            left = 0
            right = 0
            
            # right to left
            for i in range(len(s)-1, -1, -1):
                if s[i] == '(':
                    left+=1
                else:
                    right+=1
                if left == right: # valid paratheses
                    max_len = max(max_len, left * 2)
                if right < left: # invalid point
                    left, right = 0, 0
            return max_len
        return stack(s)
            