class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Solution 1: DP
        # compare nums[i] and nums[j], if curr larger than previous, prev+1 compare with cur
        # Time complexity: O(n^2)
        # Space complexity: O(n)
        # nums [3,4,1,2,8]
        #   dp [1,1,1,1,1]
        #      [1,2,1,1,1]
        #      [1,2,1,1,1]
        #      [1,2,1,2,1]
        #      [1,2,1,2,3]
        # dp = [1]*len(nums) # len of itself is 1
        # for i in range(1, len(nums)):
        #     for j in range(0, i+1): # compare with previous
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j]+1)
        # return max(dp)
    
        # Solution 2: DP + Greedy
        # for two subsequences they have same len, [1,2,3] and [1,2,5],
        # [1,2,3] is better than [1,2,5] since 3<5 so 3 have more chance to expend
        # dp[i]: the smallest ending number of subsequence that len is i+1
        # in each iter:
        #  1. expend the subsequence
        #  2. replace the smallest ending
        # nums [3,4,1,2,8,5,6]
        #   dp [3] // [3] insert at 0
        #      [3,4] // [3], [*,4] insert at 1
        #      [1,4] // [1], [*,4] insert at 0
        #      [1,2] // [1], [*,2] insert at 1
        #      [1,2,8] // [1], [*,2], [*,*,8] insert at 2
        #      [1,2,5] // [1], [*,2], [*,*,5]
        #      [1,2,5,6] // [1], [*,2], [*,*,5], [*,*,*,6]
        # dp is increasing, use binary search to find the index to insert it
        # Time complexity: O(nlogn) (Time complexity for binary search is logn)
        dp = []
        for num in nums:
            idx = bisect_left(dp, num) # find the left index to insert
            if idx == len(dp):
                dp.append(num)
            else:
                dp[idx] = num
        return len(dp)
        