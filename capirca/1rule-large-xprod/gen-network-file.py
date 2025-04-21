#! /usr/bin/env python3

import sys

first_line = True
for x1 in range(1,5):
    for x2 in range(1,251):
        if first_line:
            first_line = False
            print("SRC_1 = 10.%d.%d.0/24" % (x1, x2))
        else:
            print("        10.%d.%d.0/24" % (x1, x2))

print("")

first_line = True
for x1 in range(1,5):
    for x2 in range(1,251):
        if first_line:
            first_line = False
            print("SRC_2 = 11.%d.%d.0/24" % (x1, x2))
        else:
            print("        11.%d.%d.0/24" % (x1, x2))
