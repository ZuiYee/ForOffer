# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        if size == 0:
            return []
        index = []
        for r in range(0, len(num) - size + 1):
            l = r + size
            maximum = 0
            temp = max(num[r: l])
            if temp > maximum:
                maximum = temp
            index.append(maximum)
        return index


test = [2, 3, 4, 2, 6, 2, 5, 1]
s = Solution()
print(s.maxInWindows(test, 3))
