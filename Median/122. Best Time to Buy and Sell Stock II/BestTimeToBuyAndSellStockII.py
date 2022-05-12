class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def solution1():
            # collect all price gain
            res = 0
            for i in range(1, len(prices)):
                gain = prices[i] - prices[i-1]
                if gain > 0:
                    res += gain
            return res
        
        def solution2():
            curent_hold = 0
            current_not_hold = 0
            
            for price in prices:
                prev_hold = curent_hold
                prev_not_hold = current_not_hold
                
                curent_hold = max(prev_hold, prev_not_hold - price)
                current_not_hold = max(prev_not_hold, prev_hold + price)
                
            return current_not_hold if current_not_hold > 0 else 0
        
        return solution1()