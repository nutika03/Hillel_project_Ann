user_input = int(input('Enter your number: '))
number = int(user_input)
while number > 9:
    number_1 = [int(n) for n in str(number)]
    step = 1
    for num in number_1:
        step = step * num
        number = step
print(number)
