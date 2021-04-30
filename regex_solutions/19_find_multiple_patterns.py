import re

"""
19) Write a Python program to search some literals strings in a string. Go to the editor
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox', 'dog', 'horse'
"""
patterns = ['fox', 'dog', 'horse']
text = 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print('Searching for "%s" in "%s" ->' % (pattern, text), )
    if re.search(pattern, text):
        print('Matched!')
    else:
        print('Not Matched!')
