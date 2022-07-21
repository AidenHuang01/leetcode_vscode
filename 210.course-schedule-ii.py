#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
from typing import *
# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Construct Graph
        graph = [[] for x in range(numCourses)]
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
        
        # dfs
        path = []
        onPath = [False] * numCourses
        visited = [False] * numCourses
        self.hasCycle = False
        def dfs(graph, s):
            if onPath[s]:
                self.hasCycle = True
            if visited[s] or self.hasCycle:
                return
            onPath[s] = True
            visited[s] = True
            for i in graph[s]:
                dfs(graph, i)
            path.append(s)
            onPath[s] = False
        
        for i in range(numCourses):
            dfs(graph, i)
            if self.hasCycle:
                return []
        path.reverse()

        return path
            
        
# @lc code=end

