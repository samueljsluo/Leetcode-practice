class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:greatest = -1
        for idx in range(len(arr)-1, -1, -1):
            arr[idx], greatest = greatest, max(greatest, arr[idx])
        return arr
            