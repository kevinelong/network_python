import re


# 17) Write a Python program to check for a number at the end of a string.
def end_num(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False


print(end_num('abcdef'))
print(end_num('abcdef6'))
