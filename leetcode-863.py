#-----------------题目描述------------------
# https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree/
#------------------题解---------------------
#https://www.cnblogs.com/yeshengCqupt/p/13957796.html


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return -1
            elif node is target:
                subtree(node, 0)
                return 1
            else:
                left, right = dfs(node.left), dfs(node.right)
                if left != -1:
                    if left == K:
                        res.append(node.val)
                    subtree(node.right, left + 1)
                    return left+1
                elif right != -1:
                    if right == K:
                        res.append(node.val)
                    subtree(node.left, right + 1)
                    return right + 1
                else:
                    return -1
        def subtree(node, distance):
            if not node:
                return
            elif distance == K:
                res.append(node.val)
            else:
                subtree(node.left, distance + 1)
                subtree(node.right, distance + 1)
        dfs(root)
        return res