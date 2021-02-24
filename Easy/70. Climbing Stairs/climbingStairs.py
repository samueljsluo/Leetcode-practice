class Solution:
    def climbStairs(self, n: int) -> int:
        # 2 -> 1+1 or 2 -->2
        # 3 -> 1+1+1 or 1+2 or 2+1 -->3
        # 4 -> 1+1+1+1 or 2+2 or 1+1+2 or 1+2+1 or 2+1+1 -->5
        # curr = nums[i-1] + nums[-2]
        # [1, 1, 2, 3, 5, 8....]

        # Solution 1:
    #     dic = {1:1, 2:2}
    #     return self.helper(n, dic)
    # def helper(self, n, dic):
    #     if n not in dic:
    #         dic[n] = self.helper(n-1, dic) + self.helper(n-2, dic)
    #     return dic[n]
    
        # Solution 2:
        # DP
        # i, j = 1, 1
        # for _ in range(2, n+1):
        #     i, j = j, i+j
        # return j
        
        # Solution 3:
        # DP
        lst = [1]*(n+1)
        for idx in range(2, n+1):
            lst[idx] = lst[idx-1] + lst[idx-2]
        return lst[n]