#-------------------------题目链接----------------
#https://leetcode-cn.com/problems/find-the-most-competitive-subsequence/
#博客：https://www.cnblogs.com/yeshengCqupt/p/14057027.html
#-----------------------------------------------
import copy
class Solution:
    def mostCompetitive(self, nums, k):
        '''
        垃圾dfs
        '''
        self.res = list()
        vis = [0] * len(nums)
        r = list()
        def dfs(nums, u, r, vis):
            if u == k:
                self.res.append(copy.deepcopy(r))
                return
            for i in range(0, len(nums)):
                if vis[i] == 0:
                    r.append(nums[i])
                    vis[i] = 1
                    dfs(nums[i + 1:], u + 1, r, vis[i+1:])
                    vis[i] = 0
                    r.pop()
        dfs(nums, 0, r, vis)
        self.res.sort()
        return self.res[0]

    def mostCompetitive1(self, nums, k):
        '''
        单调栈
        '''
        stack = list()
        count = len(nums) - k
        for i in range(0, len(nums)):
            if not stack or nums[i] >= stack[-1]:
                stack.append(nums[i])
            else:
                while stack and nums[i] < stack[-1] and count != 0:
                    stack.pop()
                    count -= 1
                stack.append(nums[i])
        while count != 0:
            stack.pop()
            count -= 1
        return stack

s = Solution()
# nums = [2,4,3,3,5,4,9,6]
nums = [3,5,2,6]
k = 4
k = 2
res = s.mostCompetitive1(nums, k)
print(res)