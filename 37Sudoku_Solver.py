class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        参考LeetCode的答案写的python的题解
        https://leetcode.com/problems/sudoku-solver/discuss/15752/Straight-Forward-Java-Solution-Using-Backtracking
        https://leetcode.com/problems/sudoku-solver/discuss/15959/Accepted-Python-solution   
        """
        self.helper(board)

    def helper(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for c in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                        if self.isValid(board, i, j, c):
                            board[i][j] = c
                            if self.helper(board):
                                return True
                            board[i][j] = "."
                    return False
        return True

    def isValid(self, board, row, col, c):
        for i in range(9):
            if board[i][col] != '.' and board[i][col] == c:
                return False
            if board[row][i] != '.' and board[row][i] == c:
                return False
            new_row, new_col = 3 * (row // 3) + i // 3, 3 * (col // 3) + i % 3
            if board[new_row][new_col] != '.' and board[new_row][new_col] == c:
                return False
        return True


class Solution_0(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        上面的改进版 速率提升了
        参考LeetCode的答案写的python的题解
        https://leetcode.com/problems/sudoku-solver/discuss/15860/Compact-Python-solution-beats-70
        上面的改进版
        """
        self.rows = [[0]*9 for _ in range(9)]
        self.cols = [[0]*9 for _ in range(9)]
        self.boxs = [[0]*9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    k, num = i // 3 * 3 + j // 3, int(board[i][j]) - 1
                    self.rows[i][num] = self.cols[j][num] = self.boxs[k][num] = 1
        self.helper(board)

    def helper(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for c in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                        if self.isValid(board, i, j, c):
                            k, num = i // 3 * 3 + j // 3, int(c)-1
                            board[i][j] = c
                            self.rows[i][num] = self.cols[j][num] = self.boxs[k][num] = 1
                            if self.helper(board):
                                return True
                            board[i][j] = "."
                            self.rows[i][num] = self.cols[j][num] = self.boxs[k][num] = 0
                    return False
        return True

    def isValid(self, board, row, col, c):
        k, num = row // 3 * 3 + col // 3, int(c) - 1
        if self.rows[row][num] == 0 and self.cols[col][num] == 0 and self.boxs[k][num] == 0:
            return True
        return False


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".",
                                                         "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

s = Solution_0()
s.solveSudoku(board)
print(board)
