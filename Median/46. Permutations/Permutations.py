class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        return self.helper(nums, res, temp)
    
    def helper(self, nums, res, temp):
        if len(temp) == len(nums):
            res.append(temp[:])
            
        for i in range(len(nums)):
            if nums[i] in temp:
                continue
            temp.append(nums[i])
            self.helper(nums, res, temp)
            temp.pop()
            
        return res
