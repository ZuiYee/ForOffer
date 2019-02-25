# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        i, j = 0, len(array) - 1
        res = []
        while i < j:
            if array[i] + array[j] == tsum:
                res.append(array[i])
                res.append(array[j])
                break
            print(i, j)
            if array[i] + array[j] > tsum:
                j -= 1
            elif array[i] + array[j] < tsum:
                i += 1
        return res


array = [1, 2, 3, 4, 7, 8, 9, 11, 13, 15, 16]
s = Solution()
print(s.FindNumbersWithSum(array, 15))
