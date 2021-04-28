data = [
    {
        "type": "switch"
    },
    {
        "type": "switch"
    },
    {
        "type": "router"
    },
    {
        "type": "switch"
    },
    {
        "type": "server"
    },
    {
        "type": "switch"
    },
]
# THE HARD WAY
for item in data:
    result = ""
    if item["type"] == "switch":
        result = "Its a Switch!!!"
    elif item["type"] == "router":
        result = "Its a router!!!"
    elif item["type"] == "server":
        result = "Its a server!!!"
    else:
        result = "WARNING: Unknown type!!!"
    print(result)
print()

# DATA DRIVEN - USE A DICT TO MAP INPUT TO OUTPUT

mapping = {"switch": "Its a Switch!!!",
           "router": "Its a router!!!",
           "server": "Its a server!!!"}
for item in data:
    print(mapping[item["type"]])
print()

# SAME FOR ACTIONS/FUNCTION

mapping = {"switch": lambda x: print("FIts a Switch!!!"),
           "router": lambda x: print("FIts a router!!!"),
           "server": lambda x: print("FIts a server!!!")}
for item in data:
    value = item["type"] # pull out type to use as key to look up function
    f = mapping[value] # pull function out of dict
    f("")  # call the function and pass dummy parameter ""
    # mapping[item["type"]]("")
print()

print("Final")
# BUILD AND USE DICT INSIDE LAMDA
map(lambda item: {"switch": lambda x: print("Its a Switch!!!"),
                  "router": lambda x: print("Its a router!!!"),
                  "server": lambda x: print("Its a server!!!")}[item["type"]](item), data)
