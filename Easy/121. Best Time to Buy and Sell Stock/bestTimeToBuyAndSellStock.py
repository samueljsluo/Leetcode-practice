class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force
        # O((n-1)!)
        # res = 0
        # for i in range(0, len(prices)):
        #     for j in range(i+1, len(prices)):
        #         res = max(res, prices[j]-prices[i])
        # return res

        # DP
        # [ 7, 1, 5, 3, 6, 4]
        # track previous lowsest price and check max profit we can achieve so far
        # O(n)
        low = prices[0]
        profit = 0
        for p in prices:
            low = min(p, low)
            profit = max(profit, p-low)
        return profit
    
        # DP
        # convert to daily dain, today price-previous day price = gain
        # [ 7, 1, 5, 3, 6, 4]
        # [  ,-6, 4,-2, 3,-2]
        # find maximum subarray
        # [4,-2,3] mean if I hold this stock from second day and sell at fifth day can achieve max gain
        # O(n)
        # gain = [0]*len(prices)
        # for i in range(1, len(prices)):
        #     gain[i] = prices[i]-prices[i-1]
        # if max(gain) < 0: return 0
        # local_m, glo_m = 0, 0
        # for i in range(1, len(gain)):
        #     local_m = max(0, local_m+gain[i])
        #     glo_m = max(glo_m, local_m)
        # return glo_m
        
        # local_m, glo_m = 0, 0
        # for i in range(1, len(prices)):
        #     local_m = max(0, prices[i]-prices[i-1]+local_m)
        #     glo_m = max(glo_m, local_m)
        # return glo_m