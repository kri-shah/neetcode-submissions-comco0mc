class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            s1, e1 = res[-1]
            s2, e2 = intervals[i]
            if s2 <= e1:
                res.pop()
                res.append([s1, max(e1,e2)])
            else:
                res.append(intervals[i])
        return res