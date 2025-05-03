#! /usr/bin/env python3

import sys

# The output will contain 2^K-1 prefixes, so while this program should
# work for K up to 32, you might not want to generate a rule set that
# large.

K = 4
#K = 10
max = 1 << K

all_prefixes = []
for j in range(0, max):
    prefix_address = j << (32 - K)
    prefix_str = ("%d.%d.%d.%d/%d"
                  "" % ((prefix_address >> 24) & 0xff,
                        (prefix_address >> 16) & 0xff,
                        (prefix_address >>  8) & 0xff,
                        (prefix_address >>  0) & 0xff,
                        K))
    all_prefixes.append(prefix_str)

all_prefix_sets = []
for set_num in range(0, K):
    one_prefix_set = []
    mask = 1 << set_num
    for j in range(0, max):
        if j & mask != 0:
            one_prefix_set.append(all_prefixes[j])
    all_prefix_sets.append(one_prefix_set)

for field in ["SRC", "DST"]:
    for set_num in range(0, K):
        first_line = True
        prefix_set = all_prefix_sets[set_num]
        print("")
        for prefix in prefix_set:
            if first_line:
                first_line = False
                print("%s_%d = %s" % (field, set_num, prefix))
            else:
                print("        %s" % (prefix))
