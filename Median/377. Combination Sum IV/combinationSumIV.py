class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Solution 1: Backtracking
#         res = [0]
#         temp = []
#         self.helper(nums, target, res, temp)
#         return res[0]
        
#     def helper(self, nums, target, res, temp):
#         if sum(temp) == target:
#             res[0] +=1
#             return
#         if sum(temp) > target:
#             return
#         for n in nums:
#             temp.append(n)
#             self.helper(nums, target, res, temp)
#             temp.pop()
        
        # Solution 2: resursive with memory
        # mem = {target: number of solution}
        mem = [-1] * (target+1)
        mem[0] = 1
        return self.helper(nums, target, mem)
    
    def helper(self, nums, target, mem):
        if target < 0: return 0 # no solution
        if mem[target] != -1: return mem[target]  # had solution
        res = 0
        for n in nums:
            res+=self.helper(nums, target-n, mem)
        mem[target] = res
        return res
    
        # Solution 3: DP
        # dp = [0] * (target+1)
        # dp[0] = 1
        # for t in range(1, target+1):
        #     for n in nums:
        #         if t-n >= 0:
        #             dp[t]+=dp[t-n]
        # return dp[target]
        