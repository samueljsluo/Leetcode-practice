class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = 0
        for idx in range(len(nums)):
            if nums[idx]!=0:
                nums[temp] = nums[idx]
                temp+=1
        nums[temp:] = [0]*(len(nums)-temp)