class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:        
        left = 0
        right = len(A)-1
        res = [0]* len(A)
        while left <= right:
            if abs(A[left]) > abs(A[right]):
                res[right-left] = A[left]**2
                left+=1
            else:
                res[right-left] = A[right]**2
                right-=1
        return res
    