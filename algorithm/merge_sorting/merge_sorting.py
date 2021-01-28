def countInversions(arr):
    swap = 0
    copy = arr.copy()
    arr.sort()
    for i in range(len(arr)):
        if copy[i] > arr[i]:
            for j in range(i+1, len(arr)):
                if arr[j] != copy[i]:
                    swap += 1
                else:
                    swap += 1
                    break

    return swap


def run(file):
    file = open(file, "r+")
    t = int(file.readline())

    result = []
    for t_itr in range(t):
        n = int(file.readline())
        arr = list(map(int, file.readline().split()))
        assert n == len(arr)
        result.append(countInversions(arr))

    file.close()
    return result


if __name__ == '__main__':
    out1 = run("input_1.txt")
    print(out1)
    assert out1 == [0, 4]
