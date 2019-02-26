
class Solution:
    def quick_sort(self, a):
        if not a:
            return a
        i = a[0]
        before = self.quick_sort([x for x in a[1:] if x <= i])
        after = self.quick_sort([x for x in a[1:] if x > i])
        final = self.quick_sort(before) + [i] + self.quick_sort(after)
        return final



a = [2,3,4,1,6,7,8]
s = Solution()
print(s.quick_sort(a))
