class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Solution 1: use adjacency list
        # [[4,0], [4,1], [3,1], [3,2], [5,4], [5,3]]
        # inDegree is the number of prerequisites for each course
        # graph is {pre: take} (adjacency list)
        #        course pre  0, 1, 2, 3, 4, 5
        # inDegree would be [0, 0, 0, 2, 2, 2]
        # graph would be 
        #               0: [4]
        #               1: [4,3]
        #               2: [3]
        #               3: [5]
        #               4: [5]
        
#         inDegree = [0]*numCourses
#         graph = defaultdict(list)
#         for i in range(len(prerequisites)):
#             inDegree[prerequisites[i][0]]+=1
#             graph[prerequisites[i][1]].append(prerequisites[i][0])
        
#         # append the courses which dont need pre
#         queue = []
#         for i in range(numCourses):
#             if inDegree[i] == 0:
#                 queue.append(i)
        
#         while queue:
#             cur = queue.pop(0) #BFS
#             take = graph[cur]
#             for i in take:
#                 inDegree[i]-=1  # update inDegree
#                 if inDegree[i] == 0:  # when inDegree is zero, which mean you finish all the pre
#                     queue.append(i)
                    
#         return True if sum(inDegree) == 0 else False  # if there is pre left, means there have cycle


        # Solution 2: Topological sort
        # [[4,0], [4,1], [3,1], [3,2], [5,4], [5,3]]
        #        5
        #       / \
        #      3   4
        #     / \ / \
        #    2   1   0
        # graph would be 
        #               0: [4]
        #               1: [4,3]
        #               2: [3]
        #               3: [5]
        #               4: [5]
        # each time treverses a node and then set it to visiting, and dfs it's neighbor
        # if there is a neighbor is in visiting status, there is cycle
        
        graph = defaultdict(list)
        for i in range(len(prerequisites)):
            graph[prerequisites[i][1]].append(prerequisites[i][0])
        
        v = [0] * numCourses # 0: default, 1:visiting, 2:visited
        for i in range(numCourses):
            if self.dfs(i, v, graph): return False
        return True
    
    def dfs(self, cur, v, graph):
        if v[cur] == 1: return True # node is visiting, there is cycle
        if v[cur] == 2: return False
        
        v[cur] = 1 # node is visiting
        
        for t in graph[cur]: # DFS for this node's neighbors
            if self.dfs(t, v, graph): return True # there is cycle
            
        v[cur] = 2 # node is visited
        return False
        