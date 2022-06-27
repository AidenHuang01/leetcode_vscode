#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start

from re import L


class TrieNode:
    def __init__(self, val=''):
        self.val = val
        self.child = {}
        self.terminal = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode(val="root")
        

    def addWord(self, word: str) -> None:
        curr = self.root
        while word:
            if word[0] not in curr.child:
                node = TrieNode(word[0])
                curr.child[word[0]] = node
            else:
                node = curr.child[word[0]]
            curr = node
            word = word[1:]
        curr.terminal = True

    def search(self, word: str) -> bool:
        def recurr(root, word):
            # print(f"recurr({root.val}, {word})")
            if len(word) == 0:
                # print(f"root.val = {root.val}, root.terminal = {root.terminal}")
                if root.terminal:
                    return True
                else:
                    return False
            if word[0] == ".":
                found = False
                for child in root.child:
                    found = found or recurr(root.child[child], word[1:])
            elif word[0] not in root.child:
                return False
            else:
                return recurr(root.child[word[0]], word[1:])
            return found
        return recurr(self.root, word)

            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

