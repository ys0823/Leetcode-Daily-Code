#--------------------题目链接--------------------
#https://leetcode-cn.com/problems/n-queens/
#-----------------------------------------------------
import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.N = n
        self.res = []
        # board = ['.' for i in range(n)]
        board = [['.' for i in range(n)] for j in range(n)]
        self.backtrack(board, 0, self.res)
        return self.res

    def backtrack(self, board, row, res):
        list1 = list()
        if row == len(board):
            for i in range(len(board)):
                #print(board[i])
                list1.append(''.join(board[i]))
            res.append(copy.deepcopy(list1))
            return

        n = len(board[row])
        for i in range(n):
            if not self.isValid(board, row, i):
                continue
            board[row][i] = 'Q'
            self.backtrack(board, row + 1, res)
            board[row][i] = '.'

    def isValid(self, board, row, col):
        num = len(board)
        #同一列是否冲突
        for i in range(num):
            if board[i][col] =='Q':
                return False
        i, j = row - 1, col + 1
        #右上方是否冲突
        while i >= 0 and j < num:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        #左上方是否冲突
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        return True