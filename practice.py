from time import time
from transformations import transform

data = [
    {
        "id": 111,
        "device": "a",
        "description": "server"
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
        "description": "server"
    },
]


def find_item1(data, value):
    count = 0
    for item in data:
        count += 1
        if item["id"] == value:
            print(f"Found: {item}, in {count} loops.")
            return item


def find_item2(data, value):
    return indexed[value]


indexed = transform(data, "id")


started = time()
for _ in range(10000):
    find_item1(data, 333)
stopped = time()
print(stopped - started)

started = time()
for _ in range(10000):
    find_item2(indexed, 333)
stopped = time()
print(stopped - started)

