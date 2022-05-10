class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def solution1():  # count amount of each color then modify nums
            r, w, b = 0, 0, 0
            for n in nums:
                if n == 0:
                    r+=1
                elif n == 1:
                    w+=1
                else:
                    b+=1
            nums[:r] = [0] * r
            nums[r:r+w] = [1] * w
            nums[r+w:] = [2] * b
            
        def solution2():  # track 0 and 2's index
            l, r, zero = 0, len(nums)-1, 0
            
            while l <= r:
                if nums[l] == 0:
                    nums[l], nums[zero] = nums[zero], nums[l]
                    l+=1
                    zero+=1
                elif nums[l] == 2:
                    nums[l], nums[r] = nums[r], nums[l]
                    r-=1  # since nums[r] might be 0 or 2, left does not need to increase 1
                else:
                    l+=1
        solution1()
