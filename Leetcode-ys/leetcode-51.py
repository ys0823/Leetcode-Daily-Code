#--------------------题目链接--------------------
#https://leetcode-cn.com/problems/n-queens/
#-----------------------------------------------------
import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [['.' for i in range(n)] for j in range(n)]
        res = []
        col = [False] * n
        dg = [False] * 2 * n
        xdg = [False] * 2 * n

        def dfs(u):
            r = list()
            if u == n:
                for i in range(n):
                    r.append(''.join(copy.deepcopy(grid[i])))
                res.append(r)
                return

            for i in range(n):
                if not col[i] and not dg[u+i] and not xdg[n-u+i]:
                    grid[u][i] = 'Q'
                    col[i] = dg[u+i] = xdg[n-u+i] = True
                    dfs(u+1)
                    grid[u][i] = '.'
                    col[i] = dg[u+i] = xdg[n-u+i] = False
                    
        dfs(0)
        return res