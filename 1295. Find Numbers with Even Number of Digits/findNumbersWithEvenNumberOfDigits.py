class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # Solution 1: stringify
        # res = 0
        # for num in nums:
        #     if len(str(num))%2==0:
        #         res+=1
        # return res
        
        # Solution 2:
        # O(n*m)
        res = 0
        for num in nums:
            count = 0
            while num >= 1:
                num = num/10
                count+=1
            if count%2==0:
                res+=1
        return res
