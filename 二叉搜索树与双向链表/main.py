# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.leave = None

    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            self.leave = pRootOfTree
            return pRootOfTree

        left = self.Convert(pRootOfTree.left)
        # print(left.val)
        if left:
            self.leave.right = pRootOfTree
            pRootOfTree.left = self.leave

        self.leave = pRootOfTree

        right = self.Convert(pRootOfTree.right)
        # print(right.val)
        if right:
            right.left =pRootOfTree
            pRootOfTree.right = right
        # print("leave", self.leave.val)
        return left if left else pRootOfTree

    def Convert1(self, root):
        if not root:
            return None
        if not root.left and root.right:
            self.leave = root
            return root

        left = self.Convert(root.left)
        if left:
            self.leave.right = root
            root.left = self.leave
        self.leave = root

        right = self.Convert(root.right)
        if right:
            right.left = root
            root.right = right
        return left if left else root


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

S = Solution()
newList = S.Convert(pNode1)
while newList:
    if newList.left:
        print('left', newList.left.val)
    print(newList.val)

    newList = newList.right