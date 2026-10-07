def find_common_elements(list1, list2):
    result = []
    for value in list1:
        if value in list2 and value not in result:
            result.append(value)
    return result
    # TODO: use for loops to find values present in both list1 and list2, with no duplicates

find_common_elements([1, 2, 3], [2, 3, 4])
find_common_elements([1, 1, 2], [1, 3])
find_common_elements([1, 2], [3, 4])
find_common_elements([], [1, 2])