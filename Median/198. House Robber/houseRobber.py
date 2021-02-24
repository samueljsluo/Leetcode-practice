class Solution:
    def rob(self, nums: List[int]) -> int:
        # Solution 1: DP
        # O(n)
        # [2,1,1,2]
        #  0,1,0,1 | 3
        #  1,0,1,0 | 3
        #  0,1,1,0 | not valid
        #  1,0,0,1 | 4
        # in each iteration find current max money, use a dp to store
        # dp[i] is either dp[i-1] or dp[i] + do[i-2] depend on which one is larger
        # if not nums: return 0
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # dp = [0] + dp
        # nums = [0] + nums
        # for i in range(2, len(nums)):
        #     dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        # return dp[-1]
        
        dp1 = 0 # store i-1
        dp2 = 0 # store i-2
        for i in range(len(nums)):
            dp = max(dp2 + nums[i], dp1) # dp -> store i
            dp2 = dp1
            dp1 = dp # next iteration i would be i-1, so store to dp1
        return dp1
    
        # Solution 2: Recursive with mem
#         mem = [-1] * len(nums)
#         return self.helper(nums, mem, len(nums)-1)
        
#     def helper(self, nums, mem, i):
#         if i < 0: return 0
#         if mem[i] >=0: return mem[i]
#         mem[i] = max(self.helper(nums, mem, i-1), self.helper(nums, mem, i-2) + nums[i])
#         return mem[i]