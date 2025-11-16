general_list = [1, 2, 3, 4, 5, 6]
if len(general_list) == 0:
    result = [[], []]
    print(result)
else:
    even = len(general_list)
    if even % 2 == 0:
        two_lists = len(general_list) // 2
    else:
        two_lists = len(general_list) // 2 + 1
    first_list = general_list[:two_lists]
    second_list = general_list[two_lists:]
    result = [first_list, second_list]
    print(result)





