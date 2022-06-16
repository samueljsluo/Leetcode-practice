class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        def slidingWindow():
            # find the longest sequence in the middle
            target = sum(nums) - x
            if target == 0:
                return len(nums)
            if target < 0:
                return -1
            
            left, right, window = 0, 0, 0
            max_len = -1
            while right < len(nums):
                window+=nums[right]
                right+=1
                while window > target:
                    window-=nums[left]
                    left+=1
                if window == target:
                    max_len = max(max_len, right - left)
            return -1 if max_len == -1 else len(nums) - max_len
        
        return slidingWindow()
                