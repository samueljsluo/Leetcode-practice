class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = 1  # 要擺放的位置，因為第0個一定會是uniqe，所以從1開始
        for idx in range(len(nums)-1):
            if nums[idx] != nums[idx+1]: #判斷目前的和下一個是否一樣
                nums[temp] = nums[idx+1] 
                temp+=1 #更新要擺放的位置
        return temp