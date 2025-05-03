# Introduction

The idea of this policy is to be a difficult one for many algorithms
to implement. I believe that at least a version of
Lakshman-Stiliadis's bit-vector algorithm can handle it well, and
there may be others. Here, our goal is the following: given K groups,
how can we assign individual prefixes to the groups to maximize the 
number of resulting disjoint subgroups.

The idea is that there are K rules in the policy, for K in the range
[2, 32].

Each rule j in [1,K] has source address prefix set S(j), where each
S(j) is different from all of the others.

It is probably not necessary to make the problem challenging to
implement, but we do something similar for the dstination address
prefix sets D(j).

Every S(j) is non-empty.

Consider the set of integers {1, 2, ..., K}.  This set has 2^K
different subsets, including the empty subset.  If we omit the empty
subset, there are 2^K-1 non-empty subsets of {1, 2, ...., K}, where
one of them is the full set {1, 2, ..., K} itself.

Consider any non-empty subset X of {1, 2, ..., K}.  We want the sets
S(j) to be constructed such that there is at least one IP address A
such that:

+ for all j in X, A matches at least one prefix in S(j)
+ for all j _not_ in X, A _does not_ match any prefix in S(j)

A straightforward way to do this is to simply write down all K-bit
numbers in binary from 1 up to (2^K)-1.

For each number A, include it as a prefix in set S(j) if and only if
bit j of A is equal to 1.

By constructing a set of K prefix sets in this way, we are ensuring
that every one of the 2^K-1 sets in the Venn diagram of those K sets
has at least one prefix in it.


# Scripts

To create the two IPv4 prefix groups, run this command:

```bash
./gen-network-file.py > def/NETWORK.net
```

To create the set of rules in the policy:

```bash
./gen-pol-file.py > policies/pol/policy.txt
```
