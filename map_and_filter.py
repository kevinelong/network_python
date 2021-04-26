# Python code to illustrate cube of a number
# showing difference between def() and lambda().
def cube(y): #named function
    return y * y * y


lambda_cube = lambda y: y * y * y #an anonymous function copied into an identifier/variable

# using the normally
# defined function
print(cube(5))

# using the lambda function
print(lambda_cube(5))

print((lambda y: y * y * y)(5)) #define and call all at once.


def do_it(f):
    return f(5)


print(do_it(lambda y: y * y * y))

###

# Python code to illustrate
# filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

output = []
for item in li:
    if item % 2 != 0:
        output.append(item)
print(list(output))

final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)


#EXPECTED [5, 7, 97, 77, 23, 73, 61]
data = [
    {
        "id": 111,
        "device": "a",
        "description": "switch"
    },
    {
        "id": 222,
        "device": "bbb",
        "description": "server"
    },
    {
        "id": 333,
        "device": "ccc",
        "description": "server"
    },
    {
        "id": 444,
        "device": "ddd",
        "description": "switch"
    },
]
print(list(filter(lambda d:d["description"] == "switch", data)))
#[{'id': 111, 'device': 'a', 'description': 'switch'}, {'id': 444, 'device': 'ddd', 'description': 'switch'}]

###

# Python code to illustrate
# map() with lambda()
# to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(map(lambda x: x * 2, li))
print(final_list)

#[10, 14, 44, 194, 108, 124, 154, 46, 146, 122]

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

age = 11
print("can" if age > 21 else "can't")
