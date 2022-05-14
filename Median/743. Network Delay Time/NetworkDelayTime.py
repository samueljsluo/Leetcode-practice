class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def BFS():
            graph = defaultdict(list)
            queue = deque([(0, k)])
            cost = [0] + [float('inf')] * n   # the number of node start from 1, so add 0 at the beginning

            for u, v, w in times:
                graph[u].append((v, w))

            while queue:
                time, node = queue.popleft()
                if time < cost[node]:
                    cost[node] = time
                    for v, w in graph[node]:
                        queue.append((time + w, v))
            mx = max(cost)
            return mx if mx != float('inf') else -1
        
        def dijkstra():
            graph = defaultdict(list)
            heap = [(0, k)]  # min heap
            cost = [0] + [float('inf')] * n  # the number of node start from 1, so add 0 at the beginning
            visit = set()
            
            for u, v, w in times:
                graph[u].append((v, w))
                
            while heap:
                time, node = heapq.heappop(heap)
                if node in visit:
                    continue
                visit.add(node)
                if time < cost[node]:
                    cost[node] = time
                    for v, w in graph[node]:
                        if v in visit:
                            continue
                        heapq.heappush(heap, (time + w, v))
            return max(cost) if max(cost) != float('inf') else -1
        
        return BFS()
        