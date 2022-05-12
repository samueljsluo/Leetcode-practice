class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # key point is to focus on finding start point. dont need to travel around the circuit
        if sum(cost) > sum(gas):
            return -1
        
        start = 0
        remain = 0
        for i in range(len(gas)):
            remain += gas[i] - cost[i]
            
            if remain < 0:
                start = i + 1
                remain = 0  # start with empty tank
        return start
