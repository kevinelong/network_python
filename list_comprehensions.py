
#LIST COMPREHENSION
# newlist = [expression for item in iterable if condition == True]


#OLD
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


#NEW
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


#SIMPLE
newlist = [x for x in fruits]
print(newlist)


#RANGES
newlist = [x for x in range(10)]
print(newlist)


#TRANSFORMS
newlist = [x.upper() for x in fruits]
print(newlist)


#TERNARY
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

newlist = ["orange" if x == "banana" else x for x in fruits]
print(newlist)

#BASIC TERNARY WITHOUT LIST COMPREHENSION
age = 10
can = "yes" if age > 21 else "no"
print(can)

age = 55
can = "yes" if age > 21 else "no"
print(can)
