class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        temp = []
        res = []
        visit = [False] * len(nums)
        return self.helper(sorted(nums), res, temp, visit)
        
    def helper(self, nums, res, temp, visit):
        if len(temp) == len(nums):
            res.append(temp[:])
            
        for i in range(len(nums)):
            if visit[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and visit[i-1]:  # avoid duplicate
                continue
            temp.append(nums[i])
            visit[i] = True
            self.helper(nums, res, temp, visit)
            visit[i] = False
            temp.pop()
            
        return res
