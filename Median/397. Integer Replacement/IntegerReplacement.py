# import functools
class Solution:
    # @functools.lru_cache(None)
    def integerReplacement(self, n: int) -> int:
        memo = {1: 0, 2: 1}
        return self.helper(n, memo)
        
    def helper(self, n, memo):
        if n == 1:
            return 0
        if n in memo:
            return memo[n]
        if n % 2 == 0:
            res = self.integerReplacement(n//2) + 1
            memo[n] = res
            return res
        else:
            res = min(self.integerReplacement(n+1), self.integerReplacement(n-1)) + 1
            memo[n] = res
            return res
