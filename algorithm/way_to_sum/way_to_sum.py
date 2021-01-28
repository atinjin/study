

def way_to_sum(target, limit):
    count = [0 for _ in range(target + 1)]
    count[0] = 1

    for i in range(1, target+1):
        for m in range(1, limit+1):
            if i > m:
                if m == 1:
                    count[i] += count[i - m]
                else:
                    count[i] = count[i] + count[i - m] - count[i - m - 1]
            if i == m:
                count[i] += 1

    return count[target]


if __name__ == '__main__':
    result = way_to_sum(8, 2)
    assert result == 5, f"answer = {result}"

    result = way_to_sum(4, 2)
    assert result == 3, f"answer = {result}"

    result = way_to_sum(10, 5)
    assert result == 3, f"answer = {result}"
