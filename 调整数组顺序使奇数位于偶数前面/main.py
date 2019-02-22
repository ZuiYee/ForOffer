# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        return sorted(array, key=lambda x : x % 2, reverse=True)

S = Solution()
print(S.reOrderArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
# print(S.ReorderOddEven([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
# print(S.ReorderOddEven([-1, 2, -3, 4, -5, -6, 7, 8, 9, 10, -10]))