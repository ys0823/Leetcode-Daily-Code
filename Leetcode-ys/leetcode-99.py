#---------题目描述---------------
#https://leetcode-cn.com/problems/recover-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.x = None
        self.y = None
        self.pre = None


        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if not self.pre:
                self.pre = root
            else:
                if self.pre.val > root.val:
                    self.y = root
                    if not self.x:
                        self.x = self.pre 
                self.pre = root
            dfs(root.right)
        dfs(root)
        if self.x and self.y:
            self.x.val, self.y.val = self.y.val, self.x.val
        return root