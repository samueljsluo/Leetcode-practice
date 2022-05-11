class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def solution1():
            nums.sort()
            return nums[-k]
        
        def quickSelect():
            left = 0
            right = len(nums)-1
            while True:
                pos = partition(nums, left, right)
                if pos+1 == k:
                    return nums[pos]
                elif pos+1 > k:  # the kth largest number is on the left side
                    right = pos-1
                else:  # the kth largest number is on the right side
                    left = pos+1
                
        def partition(nums, left, right):
            pivot = nums[left]
            l = left+1
            r = right

            while l <= r:  # number larger than pivot put on the left, smaller than pivot put on the right
                if nums[l] < pivot and nums[r] > pivot:
                    nums[l], nums[r] = nums[r], nums[l]
                    l+=1
                    r-=1
                if nums[l] >= pivot:
                    l+=1
                if nums[r] <= pivot:
                    r-=1

            # put the pivot(left-most) at right position
            # since the number at position right is larger than left-most
            nums[left], nums[r] = nums[r], nums[left]  
            return r
        
        return solution1()
            