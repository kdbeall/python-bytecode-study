#!/usr/bin/env python3

# Found on stack overflow:
#    - https://stackoverflow.com/questions/32562163/how-can-i-understand-a-pyc-file-content
import dis, sys, marshal

header_size = 12 if sys.version_info >= (3, 3) else 8

with open(sys.argv[1], "rb") as file:
    magic_and_timestamp = file.read(header_size)
    code = marshal.load(file)
dis.dis(code)