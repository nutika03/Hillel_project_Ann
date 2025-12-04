import string
def is_palindrome(text):
    text = text.lower()
    chars = [char for char in text if char not in string.punctuation and char != ' ']
    texts = "".join(chars)
    return texts == texts[::-1]
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")