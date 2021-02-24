class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Solution 1:
        # if self.isPalindrome(s):
        #     return True
        # for i in range(len(s)):
        #     temp = s[:i] + s[i+1:]
        #     if self.isPalindrome(temp):
        #         return True
        # return False
        
        # Solution 2:
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left+1, right) or self.isPalindrome(s, left, right-1)
            left+=1
            right-=1
        return True
        
    def isPalindrome(self, l, left, right):
        while left < right:
            if l[left]!=l[right]:
                return False
            left+=1
            right-=1
        return True
        