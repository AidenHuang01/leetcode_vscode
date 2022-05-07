#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if not self.unit_valid(board, i, j):
                        return False
        return True
    
    def unit_valid(self,board, r, c):
        # no duplicate in the same row
        num = board[r][c]
        for i in range(9):
            if board[r][i] == num and i != c:
                return False
        for j in range(9):
            if board[j][c] == num and j != r:
                return False
        for i in range((r//3)*3, (r//3)*3+3):
            for j in range((c//3)*3, (c//3)*3+3):
                if board[i][j] == num and i != r and j != c:
                    return False
        return True

# @lc code=end

