class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'1':[], '2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'],
                   '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], 
                   '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        #backtracking O(3^m*4^n)
        if len(digits)==0:
            return []
        if len(digits)==1:
            return mapping[digits[0]]
        n = len(digits)
        res = []
        self.helper(digits, n, mapping, [], res)
        return res
        
    def helper(self, nums, n, mapping, temp, res):
        if len(temp)==n:
            res.append(''.join(temp))
            return
        for c in mapping[nums[0]]:
            temp.append(c)
            self.helper(nums[1:], n, mapping, temp, res)
            temp.pop()
        
        
        # if len(digits)==0: return []
        # if len(digits)==1: return mapping[digits[0]]
        # res = ['']
        # for d in digits:
        #     chars = mapping[d]
        #     temp = []
        #     for c in chars:
        #         for r in res:
        #             temp.append(r+c)
        #     res = temp
        # return res