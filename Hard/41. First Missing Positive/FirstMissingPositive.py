class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def brute_force():
            mx = max(nums)
            mn = 1
            for i in range(mn, mx+1):
                if i > 0 and i not in nums:
                    return i
            return mx + 1 if mx >= 0 else 1
        
        def solution2():
            n = len(nums)
            for i in range(n):
                while nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                    nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            for i in range(0, n):
                if i + 1 != nums[i]:
                    return i + 1
            return n + 1
        
        def solution3():
            nums.sort()
            res = 1
            for n in nums:
                if res == n:
                    res+=1
            return res
        return solution3()