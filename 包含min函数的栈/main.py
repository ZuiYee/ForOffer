# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)
        if self.stack2[0] > node or not self.stack2:
            self.stack2.append(node)
        else:
            temp = self.min()
            self.stack2.append(temp)
        # write code here

    def pop(self):
        if not self.stack1 or not self.stack2:
            return None
        self.stack2.pop()
        self.stack1.pop()
        # write code here

    def top(self):
        return self.stack1[-1]
        # write code here

    def min(self):
        return self.stack2[-1]
        # write code here
