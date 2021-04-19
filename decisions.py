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

mapping = {"switch": lambda x : print("Its a Switch!!!"),
           "router": lambda x : print("Its a router!!!"),
           "server": lambda x : print("Its a server!!!")}
for item in data:
    mapping[item["type"]]("")
print()

# print("Final")
# map(lambda item: {"switch": lambda x : print("Its a Switch!!!"),
#            "router": lambda x : print("Its a router!!!"),
#            "server": lambda x : print("Its a server!!!")}[item["type"]](), data)
