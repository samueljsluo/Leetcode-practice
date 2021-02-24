class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking
        # 2, 3, 6, 7
        # --->
        # if moving forward, there wont have duplicate combination
        # O(n!)
        res = []
        self.helper(candidates, res, [], target, 0)
        return res
        
    def helper(self, c, res, temp, target, index):
        if sum(temp) > target:
            return
        if sum(temp) == target:
            res.append(temp[:])
            return
        for i in range(index, len(c)):
            temp.append(c[i])
            self.helper(c, res, temp, target, i) # i is to make sure index is moving forward index
            temp.pop()