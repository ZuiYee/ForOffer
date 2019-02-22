# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if not root:
            return
        if not root.right and not root.left:
            return root
        temp = root.right
        root.right =root.left
        root.left = temp
        self.Mirror(root.left)
        self.Mirror(root.right)

