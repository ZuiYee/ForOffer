# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        if not pushV and not popV:
            return False
        stack = []
        for i in pushV:
            stack.append(i)
            print("i:", i)
            print("stack", stack)
            while len(stack) and stack[-1] == popV[0]:
                x = stack.pop()
                y = popV.pop(0)
                print(x, y)
        if len(stack):
            return False
        else:
            return True

pushV = [1, 2, 3, 4, 5]
popV = [4, 5, 3, 2, 1]
popVF = [4, 5, 2, 1, 3]
S = Solution()
print(S.IsPopOrder(pushV, popVF))