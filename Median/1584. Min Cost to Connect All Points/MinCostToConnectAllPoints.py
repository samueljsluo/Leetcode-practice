class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def solution1():
            n = len(points)
            adj_matrix = defaultdict(list)  # [dist, point]

            for i in range(n):
                x1, y1 = points[i]
                for j in range(i+1, n):
                    x2, y2 = points[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    adj_matrix[i].append([dist, j])
                    adj_matrix[j].append([dist, i])

            visit = set()
            mheap = [[0, 0]]
            res = 0

            while len(visit) < n:
                dist, point = heapq.heappop(mheap)
                if point in visit:
                    continue
                res+=dist
                visit.add(point)
                for neiDist, nei in adj_matrix[point]:
                    if nei not in visit:
                        heapq.heappush(mheap, [neiDist, nei])
            return res
        
        def solution2():
            # start from first element, so distance of first element would be zero
            dic = {(x, y): math.inf if i else 0 for i, (x, y) in enumerate(points)}
            res = 0
            visit = 0
            
            while visit < len(points):
                x, y = min(dic, key=dic.get) # current point
                visit+=1
                res += dic.pop((x, y)) # update cost
                
                # update minimum distance
                for x1, y1 in dic:
                    dic[(x1, y1)] = min(dic[x1, y1], (abs(x - x1) + abs(y - y1)))
            return res
        return solution2()
