# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        head = None
        p = pHead
        pre = None
        while p:
            next = p.next

            if not next:
                head =p
            p.next = pre
            pre = p
            p = next
        return head