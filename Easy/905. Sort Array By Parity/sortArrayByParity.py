class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # left = 0
        # right = len(A) - 1
        # idx = 0
        # res = [0]*len(A)
        # while left < len(A) and right >= 0 and idx < len(A):
        #     if A[idx]%2==0:
        #         res[left] = A[idx]
        #         left += 1
        #     else:
        #         res[right] = A[idx]
        #         right -= 1
        #     idx += 1
        # return res
    
        left = 0
        right = len(A) - 1
        while left < right:
            if A[left]%2==0:
                left+=1
            else:
                A[left], A[right] = A[right], A[left]
                right-=1
        return A
        