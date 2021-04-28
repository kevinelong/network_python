import re


# 5) Write a Python program that matches a string that has an a followed by three 'b'
def text_match(text):
    patterns = 'ab{3}?'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return 'Not matched!'


print(text_match("abbb"))
print(text_match("aabbbbbc"))
