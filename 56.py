class Interval(object):
    def __init__(self, s = 0, e = 0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        res = []
        if not intervals:
            return res
        intervals.sort(key = lambda inter : inter.start)
        s, e = intervals[0].start, intervals[0].end
        for inter in intervals[1:]:
            if inter.start > e:
                res.append(Interval(s, e))
                s, e = inter.start, inter.end
            else:
                e = max(e, inter.end)
        res.append(Interval(s, e))
        return res

intervals = Solution().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)])
for inter in intervals:
    print inter.start, inter.end
