# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        l, r =0, len(rotateArray) - 1
        while rotateArray[l] >= rotateArray[r]:
            if r - l == 1:
                return rotateArray[r]

            mid = l + (r - l) //2
            if rotateArray[l] == rotateArray[mid] ==rotateArray[r]:
                return min(rotateArray)
            if rotateArray[l] <= rotateArray[mid]:
                l = mid
            elif rotateArray[l] >= rotateArray[mid]:
                r = mid
        return rotateArray[0]


Test = Solution()
print(Test.minNumberInRotateArray([3, 4, 5, 1, 2]))
print(Test.minNumberInRotateArray([1, 2, 3, 4, 5]))
print(Test.minNumberInRotateArray([1, 1, 1, 0, 1]))
print(Test.minNumberInRotateArray([1, 0, 1, 1, 1]))
print(Test.minNumberInRotateArray([]))
print(Test.minNumberInRotateArray([1]))