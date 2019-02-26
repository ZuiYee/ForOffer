class Solution:
    def FindContinuousSequence(self, tsum):
        t1 = 1
        t2 = 2
        lis = []
        array = []
        for i in range(0, tsum+1):
            array.append(i)
        if tsum == 3:
            return [[1, 2]]
        t = 0
        while t1 <= t2 and t2 <= tsum//2 + 1:
            # print(t1,t2,t)
            t = sum(array[t1:t2+1])
            if t < tsum:
                t2 += 1
            elif t > tsum:
                t1 += 1
            elif t == tsum:
                lis.append(array[t1:t2+1])
                t = 0
                t1 += 1
        return lis



s = Solution()
print(s.FindContinuousSequence(5))
