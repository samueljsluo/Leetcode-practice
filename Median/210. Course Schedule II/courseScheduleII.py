class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Solution 1:
        # BFS
        graph = defaultdict(list)
        inDegree = [0] * numCourses
        for i in range(len(prerequisites)):
            inDegree[prerequisites[i][0]]+=1
            graph[prerequisites[i][1]].append(prerequisites[i][0])
            
        queue = []
        for i in range(numCourses):
            if inDegree[i]==0: queue.append(i)
                
        res = []
        while queue:
            cur = queue.pop(0)
            res.append(cur)
            take = graph[cur]
            for t in take:
                inDegree[t]-=1
                if inDegree[t]==0: queue.append(t)
        
        return res if sum(inDegree)==0 else []
        
        
        # Solution 2:
        # DFS with Topological sort
        # when a node is label as visited, also insert at the from or result list
        # since it is DFS, so the first added element would be the deepest node of the tree
        # O(V+E) ~ O(V^2), if it is all of the nodes are conneted it would be v^2
#         graph = defaultdict(list)
#         for i in range(len(prerequisites)):
#             graph[prerequisites[i][1]].append(prerequisites[i][0])
        
#         v = [0] * numCourses
#         res = []
#         for i in range(numCourses):
#             if self.dfs(v, i, res, graph): return []
#         return res
    
#     def dfs(self, v, cur, res, graph):
#         if v[cur] == 1: return True
#         if v[cur] == 2: return False
        
#         v[cur] = 1 # visiting
#         for i in graph[cur]:
#             if self.dfs(v, i, res, graph): return True
#         v[cur] = 2 # visited
#         res.insert(0, cur)
#         return False
