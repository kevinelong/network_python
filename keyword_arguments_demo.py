# unknown number of unnamed arguments
def print_them_all(*argv):
    for arg in argv:
        print(arg)


print_them_all('Hello', 'Welcome', 'to', 'Intermediate Python')


###

# unknown number of keyword arguments
def print_them_all(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
print_them_all(first='Happy', mid='Monday', last='Folks')
