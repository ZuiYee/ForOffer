# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    # def duplicate(self, numbers, duplication):
    #     length = len(numbers)
    #     for i in range(length):
    #         index = numbers[i]
    #         print('index1:', index)
    #         if index >= length:
    #             index -=length
    #         print('index2:', index)
    #         if numbers[index] >= length:
    #             return index
    #
    #         numbers[index] = numbers[index] + length
    #         print('numbers:', numbers)
    #     return -1
    def duplicate(self, numbers, duplication):
        length = len(numbers)
        for i in range(length):
            index = numbers[i]
            if index >= length:
                index -=length
            if numbers[index] >= length:
                duplication[0] =index
                return True

            numbers[index] = numbers[index] + length
        return False




test = [2, 3, 1, 0, 2, 5, 3]
s = Solution()
dupulication = [0]
print(s.duplicate(test,dupulication))
# print(s.duplicate2(test))