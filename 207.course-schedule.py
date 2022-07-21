#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
from typing import *
# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Construct graph
        graph = [[] for x in range(numCourses)]
        # print(graph)
        for preq in prerequisites:
            before = preq[1]
            after = preq[0]
            graph[before].append(after)
        # print(f"graph: {graph}")
        # Cycle detection
        onPath = [False] * numCourses
        visited = [False] * numCourses
        self.hasCycle = False
        def dfs(graph, s):
            
            if onPath[s]:
                self.hasCycle = True
            if visited[s] or self.hasCycle:
                return
            visited[s] = True
            onPath[s] = True
            for i in graph[s]:
                dfs(graph, i)
            onPath[s] = False
        
        for i in range(numCourses):
            dfs(graph, i)
            if self.hasCycle:
                return False
        return True

# @lc code=end

