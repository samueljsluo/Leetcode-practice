class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Solution 1:
        # nums = sorted(nums, reverse=True)
        # mx_set = set()
        # count = 0
        # for num in nums:
        #     if num not in mx_set:
        #         mx_set.add(num)
        #         count+=1
        #     if count == 3:
        #         return num
        # return max(nums)
        
        # Solution 2:
        max_set = [float('-inf'), float('-inf'), float('-inf')]
        for n in nums:
            if n not in max_set:
                if n > max_set[0]:
                    max_set = [n, max_set[0], max_set[1]]
                elif n > max_set[1]:
                    max_set = [max_set[0], n, max_set[1]]
                elif n > max_set[2]:
                    max_set = [max_set[0], max_set[1], n]
        return max(max_set) if float('-inf') in max_set else max_set[2]