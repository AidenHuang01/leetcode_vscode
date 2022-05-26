#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = {}
        dict = dict_reset(t)
        left = 0
        right = 0
        next_start = 0
        checked_index = 0
        first_hit = 0
        if len(t) == 1:
            if t in s:
                return t
            else:
                return ""
        while right < len(s):
            print(f"left: {left} right: {right} next_start: {next_start} index: {checked_index} first_hit: {first_hit} substring: {s[left:right+1]}")
            if dict_check(dict, s[right]):
                print(f"   in dict s: {s[right]} right:{right} first_hit: {first_hit} index: {checked_index}")
                checked_index += 1
                if checked_index == 1:
                    first_hit = right
                if checked_index == 2:
                    next_start = right
            if dict_empty(dict):
                print("Reached")
                print(f"result[{s[first_hit:right+1]}] = {len(s[first_hit:right+1])}")
                result[s[first_hit:right+1]] = len(s[first_hit:right+1])
                left = next_start
                right = next_start
                dict = dict_reset(t)
                checked_index = 0
                first_hit = right
            else:
                right += 1
        if result:
            min_val = float('inf')
            min_string = None
            for key in result.keys():
                if result[key] < min_val:
                    min_string = key
            return min_string
        return ""


def dict_reset(string):
    dict = {}
    for s in string:
        dict[s] = dict.get(s, 0) + 1
    return dict

def dict_check(dict, s):
    if s not in dict:
        return False
    if dict[s] == 0:
        return False
    dict[s] -= 1
    return True

def dict_empty(dict):
    for key in dict.keys():
        if dict[key] != 0:
            return False
    return True


# @lc code=end

