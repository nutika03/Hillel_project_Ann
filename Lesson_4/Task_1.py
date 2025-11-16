general_list = [1, 0, 13, 0, 0, 0, 5]
zero_count = general_list.count(0)
while 0 in general_list:
    general_list.remove(0)
zero_list = [0] * zero_count
new_list = general_list + zero_list
print(new_list)