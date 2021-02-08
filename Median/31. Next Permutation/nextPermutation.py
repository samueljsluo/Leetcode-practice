class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1,2,4,6,5,3
        # find the first number smaller than previous from end --> 4=i
        # from end, find the number which is the closet number to i --> 5=j
        # swap nums[i] and nums[j]
        # 1,2,5,6,4,3
        # reverse nums[i+1:] since it is decreasing series, after reverse it would be ascending series
        # 1,2,5,3,4,6
        
        i = len(nums) - 2
        # find the first number smaller than previous
        while i >= 0 and nums[i] >= nums[i+1]:
            i-=1
        
        # current permuation is the largest
        if i == -1:
            nums.sort()
            return
        
        # find the number which closest to i
        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[i]:
            j-=1
            
        # swap
        nums[i], nums[j] = nums[j], nums[i]
        
        # reverse
        left = i+1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1
        