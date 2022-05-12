from numpy import ones
class Solution:
    def countPrimes(self, n: int) -> int:
        def solution1():
            # Special case
            if n < 3:
                return 0
            arr = ones((n,), dtype=int)
            arr[:2] = 0

            for i in range(2,ceil(sqrt(n))):
                if arr[i]:
                    arr[i*i::i] = 0  

            return arr.sum()
        
        def solution2():
            if n < 3:
                return 0
            
            arr = [1] * n
            arr[0] = 0
            arr[1] = 0
            for i in range(2, ceil(sqrt(n))):
                if arr[i]:
                    for j in range(i*i, n, i):
                        arr[j] = 0
            return sum(arr)
        
        return solution1()
        