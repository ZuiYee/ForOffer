
class Solution:
    def Permutation(self, ss):
        print(ss)
        if not len(ss):
            return []
        if len(ss) == 1:
            return list(ss)

        charList = list(ss)
        charList.sort()
        pStr = []
        for i in range(len(charList)):
            if i > 0 and charList[i] == charList[i-1]:
                continue
            temp = self.Permutation(''.join(charList[:i])+''.join(charList[i+1:]))
            print('temp', temp)
            for j in temp:
                pStr.append(charList[i]+j)
            print('pStr', pStr)
        return pStr


ss = 'aca'
S = Solution()
print(S.Permutation(ss))
# print(S.group(ss))