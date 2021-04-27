import re

# 30) Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.
street = '21 Ramkrishna Road'
print(re.sub('Road$', 'Rd.', street))
