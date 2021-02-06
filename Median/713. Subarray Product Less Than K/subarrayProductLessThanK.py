class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # x, [x, x, x, x, x], x, x, x
        #     i           j
        # count += j-i
        # x, x, [x, x, x, x, x], x, x
        #        i           j
        # update count
        
        left = 0
        count = 0
        res = 1
        for right in range(len(nums)):
            res*=nums[right]
            while res >= k and right >= left:
                res/=nums[left]
                left+=1
            count+=right-left+1
        return count
        
        # j = 0
        # count = 0
        # product = 1
        # for i in range(len(nums)):
        #     # [10, 1, 2, 3] k=1, 10 is larger than k, so in the first iteration, prod would be 0.1 and j would smaller than i
        #     if j < i: 
        #         j=i
        #         product = 1
        #     while j < len(nums) and product*nums[j] < k:
        #         product*=nums[j]
        #         j+=1
        #     count+=j-i # x, [x, x, x, x), x, x
        #     product/=nums[i] # move left pointer, so need to divide the left pointer value
        # return count
        
        # left = 0
        # right = 1
        # count = 0
        # while left <= right <= len(nums):
        #     if prod(nums[left:right]) < k:
        #         count+=1
        #         right+=1
        #     elif prod(nums[left:right]) >= k:
        #         left+=1
        #         right = left+1
        #     if right > len(nums) and left < len(nums):
        #         left+=1
        #         right=left+1
        # return count
        