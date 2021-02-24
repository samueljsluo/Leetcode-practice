class Solution:
    def rob(self, nums: List[int]) -> int:
        # Solution 1: dp
        # if rob head, skip tail
        # if rob tail, skip head
        # [2,1,1,4]
        #  1 0 0 1 --> not valid
        # rob head --> [2,1,1] --> 3
        # rob tail --> [1,1,4] --> 5
        # select larger one
        if not nums: return 0 # edge case
        if len(nums)==1: return nums[0] # edge case
        return max(self.helper(nums, 0, len(nums)-1), self.helper(nums, 1, len(nums)))
    
    def helper(self, nums, start, end):
        dp1 = 0
        dp2 = 0
        for i in range(start, end):
            dp = max(dp2 + nums[i], dp1)
            dp2 = dp1
            dp1 = dp
        return dp1
        
        