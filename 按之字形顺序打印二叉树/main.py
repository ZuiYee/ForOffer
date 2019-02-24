class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None


class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        q1 = []
        q2 = []
        q1.append(pRoot)
        val = []
        while q1 or q2:
            val1 =[]
            while q1:
                node = q1.pop(0)
                val1.append(node.val)
                if node.left :
                    q2.append(node.left)
                if node.right :
                    q2.append(node.right)
            if val1:
                val.append(val1)
            val2 = []
            while q2:
                node = q2.pop(0)
                val2.insert(0, node.val)
                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)
            if val2:
                val.append(val2)
        return val


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
print(s.Print(pNode1))
