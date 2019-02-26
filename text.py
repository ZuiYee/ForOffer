class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        count = 1
        currentNum = 0
        for i in range(len(numbers)-1):
            if numbers[i] == numbers[i+1]:
                currentNum = numbers[i]
                count += 1
            else:
                count -= 1
            if count == 0:
                currentNum = numbers[i+1]
                count = 1
            print('count',count)
            print('currentNum',currentNum)
        count = 0
        for num in numbers:
            if num == currentNum:
                count += 1
        if 2*count > len(numbers):
            return currentNum
        else:
            return 0


x = [2,2,2,2,2,1,3,4,5]

s = Solution()
print(s.MoreThanHalfNum_Solution(x))