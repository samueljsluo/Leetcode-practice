class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        #  i    num  -5   -4   -3   -2   -1    0    1    2    3    4    5
        #  0     1                             1     
        #  1     1                        1         1
        #  2     1                   1         2         1
        #  3     1              1         3         3         1
        #  4     1         1         4         6         4         1
        #  5     1    1         5         10        10        5         1
        #DP
        ways = defaultdict(int) #key表示總和，value表示達成總和的次數
        ways[0] = 1 # store how many ways can reach the target
        for num in nums:
            temp = defaultdict(int) # store numbers of ways for next level
            for total in ways:
                temp[total+num]+=ways[total]  # temp[-1-1]+=ways[-1] 上一次次數累加
                temp[total-num]+=ways[total]
            ways = temp # 更新累加次數
        return ways[S]
        