import re

# 18) Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string.
results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 345 are important.")
print("Number of length 1 to 3")
for n in results:
    print(n.group(0))
