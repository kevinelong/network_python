
def transform(data, key="id"):
    indexed = {}
    for item in data:
        temp_id = item[key]
        # del item[key]
        indexed[temp_id] = item
    return indexed


if __name__ == "__main__":
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


    indexed = transform(data, "id")
    print(indexed)
    print(indexed[333])

