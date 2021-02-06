class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:        
        tar_dict = {val: idx for idx, val in enumerate(arr)}
        for idx, num in enumerate(arr):
            if num*2 in tar_dict and idx != tar_dict[num*2]:
                return True
        return False
        