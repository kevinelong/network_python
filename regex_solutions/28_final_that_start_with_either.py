import re

# 28) Write a Python program to find all words starting with 'a' or 'e' in a given string.
# Input.
text = "eat The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
# find all the words starting with 'a' or 'e'

# CAPTURES ALL BUT THE FIRST
result = re.findall(r"\s([ae]\w+)", text)
# Print result.
print(result)

# SPECIAL CASE FOR FIRST
result = re.findall(r"^([ae]\w+)", text)
# Print result.
print(result)

# COMBINED USING THE VERTICAL-BAR/PIPE as "OR" or "ALTERNATE" - NOT PERFECT
result = re.findall(r"(^[ae]\w+|\s[ae]\w+)", text)
# Print result.
print(result)

# BEST WITH WORD BOUNDARIES
result = re.findall(r"\b[ae]\w+", text)
# Print result.
print(result)
