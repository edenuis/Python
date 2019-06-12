#Challenge: Given a list of possibly overlapping intervals, return a new list 
#           of intervals where all overlapping intervals have been merged.
#           The input list is not necessarily ordered in any way.
#           For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should 
#           return [(1, 3), (4, 10), (20, 25)].

def sortBy(interval):
    return interval[0]

def mergeIntervals(intervals):
    new_intervals = []
    intervals = sorted(intervals, key=sortBy)
    
    for interval in intervals:
        if not new_intervals:
            new_intervals.append(interval)
        elif new_intervals[len(new_intervals)-1][1] >= interval[0] and new_intervals[len(new_intervals)-1][1] <= interval[1]:
            new_interval = (new_intervals[len(new_intervals)-1][0], interval[1])
            new_intervals.pop()
            new_intervals.append(new_interval)
        elif new_intervals[len(new_intervals)-1][1] < interval[0]:
            new_intervals.append(interval)
    return new_intervals

if __name__ == '__main__':
    print(mergeIntervals([(1, 3), (5, 8), (4, 10), (20, 25)]))
    print(mergeIntervals([(1, 3), (5, 8), (4, 10), (20, 25), (6,12)]))
    print(mergeIntervals([(1, 3), (5, 8), (4, 10), (20, 25), (6,12), (3,4)]))