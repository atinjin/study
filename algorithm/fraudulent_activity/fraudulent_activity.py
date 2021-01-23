# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

"""
0 ~ 200까지의 값을 가질 수 있다. Array 를 정렬하여 중위값을 구해야 한다.
매번 정렬하게 되면 O(N^2logN) 시간이 걸리기 때문에 실행 불가능해진다.
일정 범위의 값을 O(N) 시간내에 정렬할 수 있는 방법이 있다. -> Count Sorting
"""


def find_median_count(count_arr, d):
    """
    Count sorting
    """
    is_odd = d % 2 != 0
    if is_odd:
        median = find_median_odd(count_arr, d)
    else:
        median = find_median_even(count_arr, d)
    return median


def find_median_even(count_arr, d):
    count = 0
    target = d/2
    median = None
    for i in range(len(count_arr)):
        if count_arr[i] > 0:
            count += count_arr[i]
        if count == target:
            for j in range(i+1, len(count_arr)):
                if count_arr[j] > 0:
                    median = (i + j)/2
            break
        elif count > target:
            median = i
            break
    return median


def find_median_odd(count_arr, d):
    median = None
    first = int(d / 2) + 1
    count = 0
    for i in range(len(count_arr)):
        if count_arr[i] > 0:
            count += count_arr[i]
        if count >= first:
            median = i
            break
    return median


def activity_notifications(expenditure, d, value_range):
    notification = 0
    count_arr = []
    for a in range(value_range + 1):
        count_arr.append(0)

    # init count_arr
    for i in range(d):
        count_arr[expenditure[i]] += 1
    # find
    for j in range(d, len(expenditure)-1):
        median = find_median_count(count_arr, d)
        if expenditure[j] >= (median * 2):
            notification += 1
        count_arr[expenditure[j-d]] -= 1
        count_arr[expenditure[j]] += 1

    return notification


def run(file, answer):
    fptr = open(file, 'r+')

    nd = fptr.readline().split()
    n = int(nd[0])
    d = int(nd[1])

    expenditure = list(map(int, fptr.readline().rstrip().split()))
    fptr.close()
    assert n == len(expenditure)
    result = activity_notifications(expenditure, d, 200)

    assert (answer == result), f"{result} != collect {answer}"


if __name__ == '__main__':
    run("input_2.txt", 2)
    run("input_1.txt", 1)
    run("input_926.txt", 926)
    run("input_633.txt", 633)
