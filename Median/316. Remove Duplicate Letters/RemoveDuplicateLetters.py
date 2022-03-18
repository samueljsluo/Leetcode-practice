class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        def stack(s):
            stk = []
            for i, c in enumerate(s):
                if c not in stk:
                    # check if last element in the stack is larger than currnt char
                    # and check if the last element would appear in the rest string
                    while stk != [] and stk[-1] > c and stk[-1] in s[i+1:]:
                        stk.pop() # remove last element
                    stk.append(c)
            return ''.join(stk)
        
        def solution2(s):
            res = ''
            for i, c in enumerate(s):
                if c not in res:
                    # check if the last char of the string is larger than current char
                    # and check if the last char of the string would appear in the 
                    # rest of the string
                    while res != '' and res[-1] > c and res[-1] in s[i+1:]:
                        res = res[:-1] # remove last char
                    res+=c
            return res
        
        return solution2(s)
        