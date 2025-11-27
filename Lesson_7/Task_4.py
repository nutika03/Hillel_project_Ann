def common_elements():
    set3 = {i for i in range(100) if i % 3 == 0}
    set5 = {i for i in range(100) if i % 5 == 0}
    intersection_set = set3.intersection(set5)
    return intersection_set
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}