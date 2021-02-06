class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums = [0] + nums
        for i in range(len(nums)):
            idx = abs(nums[i])
            nums[idx] = -abs(nums[idx])
        return [i for i in range(len(nums)) if nums[i] >= 0]