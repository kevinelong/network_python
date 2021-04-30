import re


# 26) Write a Python program to match if two words from a list of words starting with letter 'P'.
words = ["Python PHP", "Java JavaScript", "c c++"]

for w in words:
    m = re.match("(P\w+)\W(P\w+)", w)
    # Check for success
    if m:
        print(m.groups())
