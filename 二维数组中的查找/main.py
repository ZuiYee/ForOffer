# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        n, m= len(array)-1, len(array[0])-1
        r = 0
        c = n
        while c>=0 and r<=m:
            if array[r][c] == target:
                return True
            elif array[r][c] > target:
                c -=1
            elif array[r][c] < target:
                r += 1
        return False