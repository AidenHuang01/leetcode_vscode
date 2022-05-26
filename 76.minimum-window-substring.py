#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "":
            return ""
        window = {}
        need = {}

        for char in t:
            need[char] = need.get(char, 0) + 1
        
        have = 0
        target = len(need)

        l = 0

        shortest_str = [-1,-1]
        shortest = float('inf')
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in need and window[s[r]] == need[s[r]]:
                have += 1
            while have == target:
                if r-l+1 < shortest:
                    shortest_str = [l, r]
                    shortest = r-l+1
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1
        
        if shortest != float('inf'):
            return s[shortest_str[0]:shortest_str[1]+1]
        return ""
            

        
# @lc code=end

