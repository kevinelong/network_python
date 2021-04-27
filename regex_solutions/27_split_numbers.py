import re

# 27) Write a Python program to separate and print the numbers of a given string.

# Sample string.
text = "Ten 10, Twenty 20, Thirty 30"
result = re.split("\D+", text)
# Print results.
for element in result:
    print(element)
