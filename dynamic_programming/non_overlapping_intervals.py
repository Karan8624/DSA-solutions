class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals = sorted(intervals , key = lambda x:x[1])
        removing = 0
        prev_end  = intervals[0][1]
        for i in range(1 , len(intervals)):
            if intervals[i][0] >= prev_end:
                prev_end  = intervals[i][1]
            else:
                removing += 1

        print(intervals)
        return removing
        