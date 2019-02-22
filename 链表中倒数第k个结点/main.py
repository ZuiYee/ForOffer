# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if head == None or k <=0:
            return None
        p1, p2 = head, head
        for i in range(k-1):
            if p1.next:
                p1 = p1.next
            else:
                return None
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        return p2


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

S = Solution()
print(S.FindKthToTail(node1, 1).val)