class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        def solution1():
            costs.sort(key= lambda x: x[0] - x[1]) # sort by different
            mid = len(costs)//2
            # first half people fly to A and second half people fly to b would be the minimun costs
            return sum([a for a, b in costs[:mid]] + [b for a, b in costs[mid:]]) 
        
        def solution2():
            # all people fly to A
            # and minus half of different which people fly to B would be less cost
            diff = []
            mid = len(costs)//2
            res = 0
            
            for item in costs:
                diff.append(item[0] - item[1])
                res+=item[0]
                
            diff.sort(reverse=True)
            for i in range(mid):
                res-=diff[i]
            return res
        
        return solution2()
        