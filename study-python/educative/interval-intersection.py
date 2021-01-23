# Given two lists of intervals, find the intersection of these two lists.
# Each list consists of disjoint intervals sorted on their start time.

def merge(intervals_a, intervals_b):
    # 정렬을 사용하기 때문에 O(NlogN) time-complexity
    intervals = intervals_a + intervals_b
    intervals.sort(key=lambda k: k[0])

    result = []
    start, end = intervals[0]
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if end >= interval[0]:
            result.append([max(start, interval[0]), min(end, interval[1])])
            start, end = min(start, interval[0]), max(end, interval[1])
        else:
            start, end = interval
    return result


def merge_better(intervals_a, intervals_b):
    """
    There are five overlapping possibilities between two intervals ‘a’ and ‘b’.
    A close observation will tell us that whenever the two intervals overlap,
    one of the interval’s start time lies within the other interval.
    This rule can help us identify if any two intervals overlap or not.
    Now, if we have found that the two intervals overlap, how can we find the overlapped part?
    Again from the above diagram, the overlapping interval will be equal to:
      start = max(a.start, b.start)
      end = min(a.end, b.end)
    That is, the highest start time and the lowest end time will be the overlapping interval.
    So our algorithm will be to iterate through both the lists together to see if any two intervals overlap.
    If two intervals overlap, we will insert the overlapped part into a result list
    and move on to the next interval which is finishing early.
    """
    idx_a, idx_b = 0, 0
    start, end = 0, 1
    result = []
    while idx_a < len(intervals_a) and idx_b < len(intervals_b):
        a, b = intervals_a[idx_a], intervals_b[idx_b]
        if (a[start] <= b[start] <= a[end]) or (b[start] <= a[start] <= b[end]):
            result.append([max(a[start], b[start]), min(a[end], b[end])])

        if a[end] > b[end]:
            idx_b += 1
        else:
            idx_a += 1
    return result


def main():
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))
    print("Intervals Intersection: " + str(merge_better([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " + str(merge_better([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()
