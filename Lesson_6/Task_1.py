import string
letters = tuple(string.ascii_letters)
user_input = input("Enter two letters with - : ")
start_letter, end_letter = user_input.split("-")
start_index = letters.index(start_letter)
end_index = letters.index(end_letter)
result = ''.join(letters[start_index : end_index + 1])
print(result)