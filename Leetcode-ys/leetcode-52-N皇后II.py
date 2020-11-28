#------------------题目链接--------------------
# https://leetcode-cn.com/problems/n-queens-ii/submissions/
#博客地址：https://www.cnblogs.com/yeshengCqupt/p/14054674.html
#--------------------------------------------------
class Solution:
    def totalNQueens(self, n: int) -> int:
        grid = [['.' for i in range(n)] for j in range(n)]
        self.res = 0
        col = [False] * n 
        dg = [False] * 2 * n 
        xdg = [False] * 2 * n 

        def dfs(u):
            if u == n:
                self.res += 1
                return 
            for i in range(n):
                if not col[i] and not dg[u+i] and not xdg[n-(u-i)]:
                    grid[u][i] = 'Q'
                    col[i] = dg[u+i] = xdg[n-u+i] = True
                    dfs(u + 1)
                    grid[u][i] = '.'
                    col[i] = dg[u+i] = xdg[n-u+i] = False
        dfs(0)
        return self.res

