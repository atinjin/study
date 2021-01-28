import sys


def closest_number(num):
    """
    https://www.hackerrank.com/challenges/closest-numbers/problem
    """

    number_list = []
    # sort numbers ascending order
    num.sort()
    # find the diff
    min_diff = sys.maxsize
    first_num = num[0]
    for n in num[1:len(num)]:
        diff = abs(first_num - n)
        if diff <= min_diff:
            min_diff = diff
            number_list = [i for i in number_list if abs(i[0]-i[1]) <= min_diff]
            number_list.append((first_num, n))
        first_num = n

    for p in number_list:
        print(p[0], p[1])

    return number_list


if __name__ == "__main__":
    result = closest_number([6, 2, 4, 10])
    answer = [(2, 4), (4, 6)]
    assert result == answer, f"expected {answer} but result is {result}"

    result = closest_number([4, 2, 1, 3])
    answer = [(1, 2), (2, 3), (3, 4)]
    assert result == answer, f"expected {answer} but result is {result}"

    result = closest_number([-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854])
    answer = [(-20, 30)]
    assert result == answer, f"expected {answer} but result is {result}"
