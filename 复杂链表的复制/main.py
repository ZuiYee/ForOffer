class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:

    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None
        head = pHead
        while head:
            node = RandomListNode(head.label)
            node.next = head.next
            head.next = node
            head = node.next
        head = pHead
        while head:
            thead = head.next
            thead.random = head.random
            head = thead.next
        head = pHead.next
        node = pHead
        while node.next:
            tmp = node.next
            node.next = tmp.next
            node = tmp

        return head

node1 = RandomListNode(1)
node2 = RandomListNode(3)
node3 = RandomListNode(5)
node1.next = node2
node2.next = node3
node1.random = node3

S = Solution()
clonedNode = S.Clone(node1)
print(clonedNode.random.label)