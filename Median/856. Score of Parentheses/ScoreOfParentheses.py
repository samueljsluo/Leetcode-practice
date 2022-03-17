class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def recursive(s):
            def score(s, l, r):
                if (r - l) == 1: return 1 # base case ()
                pair = 0
                for i in range(l, r):
                    if s[i] == '(':
                        pair+=1
                    if s[i] == ')':
                        pair-=1
                    if pair==0:
                        # (A) + (B)
                        return score(s, l, i) + score(s, i+1, r)
                return 2 * score(s, l+1, r-1) # (())
            return score(s, 0, len(s)-1)
        
        def distributiveLaw(s):
            # base case () = 2 = 2^(1-1)
            # (()()) = (()) + (()) = 2^(2-1) + 2^(2-1) = 2 + 2 = 4
            # (()(())) = (()) + ((())) = 2^(2-1) + 2^(3-1) = 2 + 4 = 6
            #
            res = 0
            power = -1
            for i in range(len(s)):
                if s[i] == '(':
                    power+=1
                else:
                    power-=1
                if s[i] == '(' and s[i+1] == ')':
                    # res += 1 << power
                    res += pow(2, power)
            return res
        
        def stack(s):
            stk = []
            score = 0
            for i in range(len(s)):
                if s[i] == '(':
                    stk.append(score)
                    score = 0 # start over
                else:
                    if score != 0:
                        score*=2 # (())
                    else:
                        score = 1 # ()
                    score = score + stk.pop() # ()()
            return score
                        
        return stack(s)
        