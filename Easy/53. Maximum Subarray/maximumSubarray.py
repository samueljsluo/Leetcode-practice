class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Solution 1:
        # [-2,1,-3,4,-1,2,1,-5,4]
        # [ 0,1, 0,4, 3,5,6, 1,5] local
        # if max(nums) < 0: return max(nums)
        # local_max, global_max = 0, 0  # since the maximum would larger than 0, default value can be 0
        # for num in nums:
        #     local_max = max(0, local_max+num)
        #     global_max = max(global_max, local_max)
        # return global_max
        
        # Solution 2:
        # [-2,1,-3,4,-1,2,1,-5,4]
        # [-2,1,-2,4, 3,5,6,-1,4]
        # use a list to store sum
        # if previous sum dp[i-1] < 0, dp[i] would be nums[i]
        # otherwise dp[i] would be dp[i-1] + nums[i]
        dp = [nums[0]] + [0]*(len(nums)-1)
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)