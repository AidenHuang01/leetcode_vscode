#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# @lc code=start

class TrieNode:
    def __init__(self, val=''):
        self.val = val
        self.child = {}
        self.terminal = False
        
class Trie:
        
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
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
        curr = self.root
        while word:
            if word[0] not in curr.child:
                return False
            curr = curr.child[word[0]]
            word = word[1:]
        if not curr.terminal:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        while prefix:
            if prefix[0] not in curr.child:
                return False
            curr = curr.child[prefix[0]]
            prefix = prefix[1:]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

