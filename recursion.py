# RECURSION IS YET ANOTHER KIND OF LOOP - BUT CRAZIER

def call_me(number):
    print(number)
    if number < 10:
        number += 1
        call_me(number)


call_me(1)

# RECURSION IS GOOD FOR TREES - like file system or deep data structures (e.g. dicts of dicts of dicts...)
tree_data = {
    "name": "",
    "type": "directory",
    "children": [
        {
            "name": "foo",
            "type": "directory",
            "children": [
                {
                    "name": "bar",
                    "type": "directory",
                    "children": [
                        {
                            "name": "stooges",
                            "type": "directory",
                            "children": [
                                {
                                    "name": "larry",
                                    "type": "file",
                                    "children": [

                                    ]
                                }, {
                                    "name": "moe",
                                    "type": "file",
                                    "children": [

                                    ]
                                }, {
                                    "name": "curly",
                                    "type": "file",
                                    "children": [

                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}


def traverse(node):
    print(node["name"])
    if "children" in node:
        for c in node["children"]:
            traverse(c)


traverse(tree_data)


def traverse2(node, depth=0):
    print(depth, node["name"])
    depth += 1

    if "children" in node:
        for c in node["children"]:
            traverse2(c, depth)


traverse2(tree_data)


def traverse3(node, depth=0, path=[]):
    path.append(node["name"])
    print(depth, node["name"], "/".join(path))
    depth += 1

    if "children" in node:
        for c in node["children"]:
            traverse3(c, depth, path)
    path.pop()  # as we exit we should throw away the last item in the path because we are moving back up the tree.


traverse3(tree_data)


def traverse4(node, depth=0, path=[], output=[], search_type="type", search_value="file"):
    path.append(node["name"])
    print(depth, node["name"], "/".join(path))
    depth += 1

    if search_type in node and node[search_type] == search_value:
        output.append(node)

    if "children" in node:
        for c in node["children"]:
            traverse4(c, depth, path, output)
    path.pop()  # as we exit we should throw away the last item in the path because we are moving back up the tree.
    return output


output = traverse4(tree_data)
print(len(output))
print(output)
