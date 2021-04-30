import re


# 8) Write a Python program to find the sequences of one upper case letter followed by lower case letters.
def text_match(text):
    patterns = '^[a-z]+_[a-z]+$'
    if not re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))
