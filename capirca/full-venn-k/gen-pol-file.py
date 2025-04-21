#! /usr/bin/env python3

import sys

# The output will contain 2^K-1 prefixes, so while this program should
# work for K up to 32, you might not want to generate a rule set that
# large.

K = 4
#K = 10
max = 1 << K

for rule in range(0, K):
    print("")
    print("term accept-web-services%d {" % (rule))
    print("  source-address:: SRC_%d" % (rule))
    print("  destination-address:: DST_%d" % (rule))
    print("  destination-port:: WEB_SERVICES")
    print("  protocol:: tcp")
    print("  action:: accept")
    print("}")
