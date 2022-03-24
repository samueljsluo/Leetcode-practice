class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        def solution1(people):
            i = 0
            j = len(people) - 1
            people = sorted(people, reverse=True)
            res = 0
            while i <= j:
                if people[i] + people[j] <= limit:
                    i+=1
                    j-=1
                else:
                    i+=1
                res+=1
            return res
        
        def solution2(people):
            i = 0
            j = len(people) - 1
            people = sorted(people, reverse=True)
            res = 0
            while i <= j:
                if people[i] + people[j] <= limit:
                    j-=1
                i+=1
                res+=1
            return res
        
        return solution2(people)
        