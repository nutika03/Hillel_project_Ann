my_lst = [12, 3, 4, 10, 8]
if len(my_lst) <= 1:
    print(my_lst)
else:
    print([my_lst[-1]] + my_lst[:-1])


