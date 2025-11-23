import string
hashtag = input("Enter your hashtag: ")
for char in string.punctuation:
    hashtag = hashtag.replace(char, '')
hashtag_split = hashtag.split()
hashtag_title = [word.title() for word in hashtag_split]
hashtag_add = '#' + ''.join(hashtag_title)
my_hashtag = hashtag_add[:140]
print(my_hashtag)