general_list = [1, 3, 5]
if len(general_list) == 0:
    result = 0
    print(result)
else:
    total_sum = sum(general_list[::2])
    last_element = general_list[-1]
    result = total_sum * last_element
    print(result)

