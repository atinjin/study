
def count_operation(anagram):
    str_len = len(anagram)
    if str_len == 0 or str_len % 2 == 1:
        return -1
    half_idx = int(str_len / 2)
    first = anagram[0:half_idx]
    second = anagram[half_idx:str_len]
    count_map = count_char(second)
    count = count_convert_operations(first, count_map)
    print(f"{first} / {second}, n(operation)={count}")
    return count


def count_convert_operations(first, count_map):
    """
    12 3 3 3 3       345612
    :param first:
    :param count_map:
    :return:
    """
    count = 0
    for c in first:
        cur_count = count_map.get(c, 0)
        if cur_count > 0:
            count_map[c] -= 1
        else:
            count += 1

    return count


def count_char(anagram):
    counter = {}
    for c in anagram:
        count = counter.get(c, 0)
        counter[c] = count + 1
    return counter


if __name__ == "__main__":
    result = count_operation("123456")
    answer = 3
    assert result == answer, f"expected {answer} result = {result}"

    result = count_operation("786678")
    answer = 0
    assert result == answer, f"expected {answer} result = {result}"