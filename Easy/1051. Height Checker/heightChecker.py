class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # [1, 1, 4, 2, 1, 3]
        # freq [0, 3, 4, 5, 6, 0]
        # [0, 0, 0, 0, 0, 0]
        # [0, 0, 1, 0, 0, 0]
        # [0, 1, 1, 0, 0, 0]
        # [0, 1, 1, 0, 0, 4]
        # [0, 1, 1, 2, 0, 0]
        # [1, 1, 1, 2, 0, 4]
        # [1, 1, 1, 2, 3, 4]

        freq = [0] * (max(heights)+1)
        for h in heights: freq[h]+=1 # create frequency of each number as a list
        for i in range(1, len(freq)): freq[i]+=freq[i-1] # add the previous frequency for index
        
        res = [0] * len(heights)
        for h in heights:
            res[freq[h]-1] = h
            freq[h]-=1
        return sum(x!=y for x, y in zip(res, heights))
            