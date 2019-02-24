class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None


class Solution:
    def Serialize(self, root):
        serializeStr = ''
        if not root:
            return '#'
        stack = []
        while root or stack:
            while root:
                serializeStr += str(root.val) + ','
                stack.append(root)
                root = root.left
            serializeStr += '#,'
            root = stack.pop()
            root = root.right
        serializeStr = serializeStr[:-1]
        return serializeStr

    def Deserialize(self, s):
        serialize = s.split(',')
        tree, sp = self.deserialize(serialize, 0)
        return tree

    def deserialize(self, s, sp):
        if sp >= len(s) or s[sp] == '#':
            return None, sp + 1
        node = TreeNode(int(s[sp]))
        sp += 1
        node.left, sp = self.deserialize(s, sp)
        node.right, sp = self.deserialize(s, sp)
        return node, sp


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
print(s.Serialize(pNode1))

x = '8,6,5,#,#,7,#,#,10,9,#,#,11,#'
print(s.Deserialize(x))