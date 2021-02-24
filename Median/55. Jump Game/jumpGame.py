class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Solution 1: DP
        # use a max to store currently you can jump the farest distance
        # if current index is larger than max, which means you are not able to reach here, return False
        mx = 0
        for i in range(len(nums)):
            if i > mx: return False
            able = i+nums[i] # the distance you can jump so far
            mx = max(mx, able)
            if mx >= len(nums)-1:
                return True
        return False
                        
                            
        