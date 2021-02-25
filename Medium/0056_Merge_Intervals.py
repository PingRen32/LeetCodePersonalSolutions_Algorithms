# Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda intervals: intervals[0])
        print(intervals)

        curr = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= curr[1]:
                curr[1] = max(intervals[i][1], curr[1])
            else:
                res.append(curr)
                curr = intervals[i]

        res.append(curr)
        return res
