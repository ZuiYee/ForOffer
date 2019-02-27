class Solution:
    def maxInWindows(self, num, size):
        res = []
        s = []
        for i in range(0, len(num)):
            print('i:', i)
            print('res0', res)
            print('s0', s)
            print()
            while len(s) > 0 and num[s[len(s)-1]] <= num[i]:
                s.pop()
            print('res', res)
            print('s', s)
            print()
            while len(s) > 0 and i - s[0] + 1 > size:
                s.pop(0)
            print('res1', res)
            print('s1', s)
            print()
            s.append(i)
            if size and i + 1 >= size:
                res.append(num[s[0]])
            print('res2', res)
            print('s2', s)
            print()
            print()
        return res


# test = [2, 3, 4, 2, 6, 2, 5, 1]
test = [2,3,4,2,6,2,5,1]
s = Solution()
print(s.maxInWindows(test, 3))


# test1 = [2, 3, 4, 2, 6, 2, 5, 1]
# print(s.maxInWindows(test, 3))