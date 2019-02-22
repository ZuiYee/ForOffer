# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n>0:
            if n & 1 == 1:
                count += 1
            n = n>>1
        return count