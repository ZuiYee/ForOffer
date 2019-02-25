# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     # 返回二维列表，内部每个列表表示找到的路径
#
#     def Find(self, root, expectNumber, lis, lisAll):
#         lis.append(root.val)
#         expectNumber -= root.val
#         if expectNumber == 0 and not root.left and not root.right:
#             lisAll.append(lis)
#             print(11, lisAll)
#         if root.left:
#             self.Find(root.left, expectNumber, lis, lisAll)
#         if root.right:
#             self.Find(root.right, expectNumber, lis, lisAll)
#         lis.pop()
#         return lisAll
#
#     def FindPath(self, root, expectNumber):
#         lis = []
#         listAll = []
#         if not root:
#             return listAll
#         return self.Find(root, expectNumber, lis, listAll)
import copy
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def Find(self, root, num, path, lis):
        path.append(root.val)
        num -= root.val
        if num == 0 and not root.left and not root.right:
            lis.append(copy.deepcopy(path))
        if root.left:
            lis = self.Find(root.left, num, path, lis)
        if root.right:
            lis = self.Find(root.right, num, path, lis)
        path.pop()
        return lis

    def FindPath(self, root, expectNumber):
        if not root:
            return []
        if expectNumber == 0:
            return []
        lis = []
        path = []
        lis = self.Find(root, expectNumber, path, lis)
        return lis


pNode1 = TreeNode(10)
pNode2 = TreeNode(5)
pNode3 = TreeNode(12)
pNode4 = TreeNode(4)
pNode5 = TreeNode(7)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5

S = Solution()
print(S.FindPath(pNode1, 22))
