# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        if number ==0:
            return 2
        f = lambda x:1 if x < 2 else f(x-2) + f(x -1)
        return f(number)

    def jumpFloor1(self, number):
        # write code here
        N1 = 2
        N2 = 1
        if number == 1:
            return 1
        if number == 2:
            return 2
        while number > 2:
            N1 = N1 + N2
            N2 = N1 - N2
            number = number - 1

        return N1


test = Solution()
print(test.jumpFloor(0),test.jumpFloor1(0))
print(test.jumpFloor(1),test.jumpFloor1(1))
print(test.jumpFloor(2),test.jumpFloor1(2))
print(test.jumpFloor(3),test.jumpFloor1(3))
print(test.jumpFloor(4),test.jumpFloor1(4))
print(test.jumpFloor(5),test.jumpFloor1(5))
print(test.jumpFloor(6),test.jumpFloor1(6))
print(test.jumpFloor(7),test.jumpFloor1(7))