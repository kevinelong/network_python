text = "192.168.1.1"

parts = text.split(".")

print(parts)

for item in parts:  # this makes a copy of each item
    item = int(item)  # this modify the copy leaving the orginal part intact

print(parts)

# SOLUTION IS TO ACCESS THE ORIGINAL BY INDEX

for i in range(len(parts)):  # use range to cycle through the indexes
    parts[i] = int(parts[i])  # modify the original in place

print(parts)

# PRINT BINARY THE LONG WAY
count = 0
for item in parts:
    b = bin(item)
    truncated = b[2:]  # slice operator
    padded = truncated.zfill(8)
    if count == len(parts) - 1:  # the last part
        print(padded)
    else:
        print(padded, end=".")
    count += 1


# PRINT BINARY THE SHORT WAY - ALL IN ONE LINE
print(".".join(map(lambda x: bin(x)[2:].zfill(8), parts)))


# COMPROMISE


def bin_pad(x):
    text = bin(x)
    sliced = text[2:]
    padded = sliced.zfill(8)
    return padded


print(".".join(map(bin_pad, parts)))
