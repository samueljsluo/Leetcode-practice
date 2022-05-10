class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        temp = []
        res = []
        return self.helper(k, n, temp, res, 1)
        
    def helper(self, k, n, temp, res, i):
        if len(temp) > k or sum(temp) > n:
            return
        
        if len(temp) == k and sum(temp) == n:
            res.append(temp[:])
            
        for i in range(i, 10):
            temp.append(i)
            self.helper(k, n, temp, res, i+1)
            temp.pop()
        return res
