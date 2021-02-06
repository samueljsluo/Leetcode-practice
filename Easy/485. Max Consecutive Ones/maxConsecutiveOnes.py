class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:        
        max_len = 0
        temp = 0
        if len(nums) == 1: return 0 if nums[0] == 0 else 1
        for n in nums:
            if n == 1:
                temp +=1
                max_len = max(max_len, temp)
            else:
                temp = 0
        return max_len
        