import keyword
import string
name = input("Enter your name: ")
if name[0].isdigit():
    print(False)
elif name != name.lower():
    print(False)
elif any(char in string.punctuation.replace('_', '') for char in name):
    print(False)
elif name in keyword.kwlist:
    print(False)
elif '__' in name:
    print(False)
else:
    print(True)