class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort()
        res = []
        for i in intervals:
            if not res or i[0] > res[-1][1]: # if last element[1] smaller than interval[0], which means no overlap
                res.append(i)
            else:  # there is overlap, merge interval
                res[-1][1] = max(res[-1][1], i[1])
        return res
        