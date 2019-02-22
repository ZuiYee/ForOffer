# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        f = lambda x: x if x <2 else f(x-1) + f(x-2)
        return f(n)

# class Solution:
#     def Fibonacci(self, n):
#         if n <=1:
#             return n
#         if n==2:
#             return 1
#         p, m, r = 1, 1, 0
#         for i in range(3,n+1):
#             r = p + m
#             p = m
#             m = r
#         return r


test = Solution()
print(test.Fibonacci(39))
print(test.Fibonacci(1))
print(test.Fibonacci(2))
print(test.Fibonacci(3))
print(test.Fibonacci(4))
print(test.Fibonacci(5))
print(test.Fibonacci(6))
print(test.Fibonacci(7))
print(test.Fibonacci(8))
print(test.Fibonacci(9))
# print(test.jumpFloor(3))
# print(test.jumpFloorII(2))