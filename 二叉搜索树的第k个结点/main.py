# -*- coding:utf-8 -*-
"""
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode

    def KthNode1(self, pRoot, k):
        if not pRoot or k == 0:
            return None
        res = self.KthNode(pRoot)
        if len(res) < k:
            return None
        else:
            return res[k - 1]

    def KthNode(self, pRoot):
        res = []
        if not pRoot:
            return None
        if pRoot.left:
            res.extend(self.KthNode(pRoot.left))
        res.append(pRoot.val)
        if pRoot.right:
            res.extend(self.KthNode(pRoot.right))
        return res


pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

s = Solution()
print(s.KthNode1(pNode1, 0))
print(s.KthNode1(pNode1, 1))
print(s.KthNode1(pNode1, 2))
print(s.KthNode1(pNode1, 3))
print(s.KthNode1(pNode1, 4))
print(s.KthNode1(pNode1, 5))
print(s.KthNode1(pNode1, 6))
print(s.KthNode1(pNode1, 7))
