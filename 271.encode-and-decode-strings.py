class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        encoded = ''
        for i in range(len(strs)):
            if strs[i] == ':':
                encoded += '::'
            else:
                encoded += strs[i]
            if i != len(strs) - 1:
                encoded += ':;'
        return encoded
            

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        decoded = []
        split_list = str.split(':;')
        for word in split_list:
            if ':' in word:
                word.remove(':')
        return split_list
