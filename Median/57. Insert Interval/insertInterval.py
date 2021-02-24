class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # find the index where to insert new interval, and do the merge
        insert_idx = len(intervals)
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                insert_idx = i
                break
        intervals.insert(insert_idx, newInterval)
        res = []
        for i in intervals:
            if not res or i[0] > res[-1][1]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
        return res