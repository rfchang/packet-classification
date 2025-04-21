# Introduction

This policy is quite simple: 1 rule.  Its source group contains
1,000 IPv4 prefixes, and its dest group contains 1,000 IPv4 prefixes.

If an implementation uses a cross product to create 1,000 x 1,000 =
1,000,000 TCAM entries, there are no production systems I am aware of
that have TCAMs with that many entries, so they would fail to fit.

There are many other algorithms that could successfully fit such a
rule easily.  This policy will not help distinguish among those
implementations.


# Scripts

To create the two IPv4 prefix groups, run this command:

```bash
./gen-network-file.py > def/NETWORK.net
```
