#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#
from typing import *
# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Construct Graph
        # define dfs
        # remove edge and trest if ther is cycle
        parent = [i for i in range(len(edges)+1)]
        weight = [1 for i in range(len(edges)+1)]
        # UnionFind algorithm
        def findParent(n):
            p = parent[n]
            while not parent[p] == p:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        for pair in edges:
            a = pair[0]
            b = pair[1]
            pa = findParent(a)
            pb = findParent(b)
            # print(f"a={a}, b={b}, len(parent)={len(parent)}")
            if pa == pb:
                return pair
            if weight[pa] > weight[pb]:
                weight[pa] += weight[pb]
                parent[pb] = pa
            else:
                weight[pb] += 1
                parent[pa] = pb


# @lc code=end

