import re

# 28) Write a Python program to find all words starting with 'a' or 'e' in a given string.
# Input.
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
# find all the words starting with 'a' or 'e'
result = re.findall("[ae]\w+", text)
# Print result.
print(result)
