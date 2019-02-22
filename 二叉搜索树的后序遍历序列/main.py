# -*- coding:utf-8 -*-
class Solution:
    def Judge(self, sequence, l, r):
        if l >=r:
            return True
        i = r
        while i > l and sequence[i - 1] > sequence[r]:
            i = i - 1
        print(i, l, r)
        for j in range(l, i):
            if sequence[j] > sequence[r]:
                return False
        return self.Judge(sequence, l, i-1) and self.Judge(sequence, i, r-1)



    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        return self.Judge(sequence, 0, len(sequence) - 1)



array = [5, 7, 6, 9, 11, 10, 8]
array2 = [4, 6, 7, 5]
array3 = [1, 2, 3, 4, 5]
S = Solution()
print(S.VerifySquenceOfBST(array))
print(S.VerifySquenceOfBST(array2))
print(S.VerifySquenceOfBST(array3))


