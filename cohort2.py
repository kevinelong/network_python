# TYPES

# x = 5  # int
# s = "hello world"  # str
# y = [1, 2, 3]  # list
#
# print(type(x))
# print(type(s))
# print(type(y))
# print(isinstance(s, str))
# class IP:
#     def __init__(self):
#         pass
# ip = IP()
# if isinstance(ip, IP):
#     print("Its an IP!")

# EXPECTED:
# <class 'int'>
# <class 'str'>
# <class 'list'>
# True

# CONVERTING OR CASTING - WHEN AND WHY
text = "10.25"

print(text * 2)
print("*" * 80)

number = float(text)
print(number * 2)

text2 = str(number)
print(text2 * 2)

r = range(10)
print(r)  # shows iterable object not the content
print(list(r))

#SYNTACTIC SUGAR for creating instances of lists and dicts
data = []  # list()
stuff = {}  # dict()

print(type(data))
print(type(stuff))
