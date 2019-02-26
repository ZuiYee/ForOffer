class Solution:
    def FindContinuousSequence(self, tsum):
        t1 = 1
        t2 = 2
        lis = []
        array = []
        for i in range(1, tsum // 2):
            array.append(i)
        if tsum == 3:
            return [1, 2]
        t = 0
        while t1 <= t2:
            print(t1, t2, t, tsum)
            t = sum(array[t1:t2])
            print(t)
            if t < tsum:
                t2 += 1
            elif t > tsum:
                t1 += 1
            elif t == tsum:
                lis.append(array[t1:t2])
                t = 0
                t2 += 1
        return lis


s = Solution()
print(s.FindContinuousSequence(4))
