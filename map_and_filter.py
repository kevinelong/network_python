# Python code to illustrate cube of a number
# showing difference between def() and lambda().
def cube(y):
    return y * y * y


lambda_cube = lambda y: y * y * y

# using the normally
# defined function
print(cube(5))

# using the lambda function
print(lambda_cube(5))

print((lambda y: y * y * y)(5))
###

# Python code to illustrate
# filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)

###

# Python code to illustrate
# map() with lambda()
# to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(map(lambda x: x * 2, li))
print(final_list)

###

# Python program to demonstrate
# use of lambda() function
# with map() function
animals = ['dog', 'cat', 'parrot', 'rabbit']

# here we intend to change all animal names
# to upper case and return the same
uppered_animals = list(map(lambda animal: str.upper(animal), animals))
print(uppered_animals)

uppered_animals = list(map(lambda animal: animal.upper(), animals))
print(uppered_animals)

uppered_animals = list(map(str.upper, animals))
print(uppered_animals)

###

# Python code to illustrate
# reduce() with lambda()
# to get sum of a list

from functools import reduce

li = [5, 8, 10, 20, 50, 100]
total = reduce(lambda x, y: x + y, li)
print(total)


###

# python code to demonstrate working of reduce()
# with a lambda function

# initializing list
lis = [1, 3, 24, 12, 2, 6]

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(reduce(lambda a, b: a if a > b else b, lis))

age = 53
print("can" if age > 21 else "can't")
