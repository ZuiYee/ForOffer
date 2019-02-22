# -*- coding:utf-8 -*-
import heapq
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput) < k:
            return []
        res = []
        for i in tinput:
            heapq.heappush(res, -i) if len(res) < k else heapq.heappushpop(res, -i)
        return sorted(list(map(lambda x: -x, res)))