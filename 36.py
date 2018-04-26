
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        https://www.cnblogs.com/zhuifengjingling/p/5277555.html
        """
        row = [[] for _ in range(9)]
        col = [[] for _ in range(9)]
        area = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    k = i // 3 * 3 + j // 3
                    if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in area[k]:
                        return False
                    else:
                        row[i].append(board[i][j])
                        col[j].append(board[i][j])
                        area[k].append(board[i][j])
        return True


import collections


# 这道题sp大神的解法在python3下都无法通过
class Solution_0:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        sp大神的解法 这个无法再python3通过
        https://leetcode.com/problems/valid-sudoku/discuss/15460/1-7-lines-Python-4-solutions
        """
        return 1 == max(collections.Counter(
            x
            for i, row in enumerate(board)
            for j, col in enumerate(row)
            if col != '.'
            for x in ((col, i), (j, col), (i/3, j/3, col))
        ).values() + [1])


class Solution_1:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        sp大神的解法
        https://leetcode.com/problems/valid-sudoku/discuss/15460/1-7-lines-Python-4-solutions
        """
        seen = set()
        return not any(x in seen or seen.add(x)
                       for i, row in enumerate(board)
                       for j, c in enumerate(row)
                       if c != '.'
                       for x in ((c, i), (j, c), (i/3, j/3, c)))
