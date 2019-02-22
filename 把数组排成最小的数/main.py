class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        numstr = map(str, numbers)  # 用str方式将int型数字转换成string
        l = lambda n1, n2: int(n1 + n2) - int(n2 + n1)  # 指定比较方式
        numsort = sorted(numstr, cmp=l)  # 用特定的比较方式进行比较
        return "".join(i for i in numsort)


numbers = [3, 32, 321]
s = Solution()
print(s.PrintMinNumber(numbers))
