class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        left = 0
        right = len(A)-1
        while left < right and A[left] < A[left+1]: left+=1
        while right >0 and A[right] < A[right-1]: right-=1
        return 0 < right==left < len(A)-1