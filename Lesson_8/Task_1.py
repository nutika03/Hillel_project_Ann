def add_one(some_list):
    number_str = ""
    for num in some_list:
        number_str += str(num)
    number = int(number_str) + 1
    result_str = str(number)
    result_list = []
    for char in result_str:
        result_list.append(int(char))
    return result_list
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")