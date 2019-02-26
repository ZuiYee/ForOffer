# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return self.Search(data, k + 0.5) - self.Search(data, k - 0.5)

    def Search(self, data, num):
        l = 0
        r = len(data) - 1
        while l <= r:

            mid = (r - l) // 2 + l
            if data[mid] > num:
                r = mid - 1
            elif data[mid] < num:
                l = mid + 1
            print(l, r)
        return l

s = Solution()
data = [1,2,3,3,3,3,4,5]
print(s.GetNumberOfK(data,3))