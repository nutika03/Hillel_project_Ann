number_1 = int(input('Enter number 1: '))
number_2 = int(input('Enter number 2: '))
operation = input('Enter operation: ')
if operation == '+':
    result = number_1 + number_2
    print(result)
elif operation == '-':
    result = number_1 - number_2
    print(result)
elif operation == '*':
    result = number_1 * number_2
    print(result)
elif operation == '/':
    if number_2 != 0:
        print(number_1 / number_2)
    else:
        print("ERROR")
else:
    print("I don't know this operation")
