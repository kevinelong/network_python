
name = "kevin"
age = 53

text = "Hello %s" % name
print(text)

text = "Hello %s is age %d" % (name, age)
print(text)


print("""
    Starting network audit script
    Device count: %d
    Threads: %d
    Device type: %s
    Commands: %s
    Output file: %s
    """ % (123, 456, "device_type", "', '.join(commands)", "filename"))
