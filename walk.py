import os
from confparse0 import parse

# Set the directory you want to start from
rootDir = '.'
for dirName, subdirList, fileList in os.walk(rootDir):
    # print('Found directory: %s' % dirName)
    for fname in fileList:
        if fname.endswith(".conf"):
            print(f'\t{dirName} {fname}')
            parse(dirName + "\\" + fname)
