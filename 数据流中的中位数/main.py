# -*- coding:utf-8 -*-
'''
数据流中的中位数
题目描述
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
'''


class Solution:
    def __init__(self):
        self.p = []
        self.q = []

    def Insert(self, num):
        if not self.p or num <= self.p[0]:
            self.p.append(num)
        else:
            self.q.append(num)
        if len(self.p) == len(self.q) + 2:
            self.q.append(p[0])
            self.p.pop(0)
        if len(self.p) + 1 == len(self.q):
            self.p.append(self.q[0])
            self.q.pop(0)


    def GetMedian(self):
        if len(self.p) == len(self.q):
            return float((self.p[0] + self.q[0]))/2
        else:
            return self.p[0]
