#!/usr/bin/env python
# -*- coding: utf-8 -*-
GOLD = "G"
LEAD = "L"

def has_gold(K,C,S,i,q):
	print "Has gold? {},{},{}".format(K,C,S)
	query_range_first = int(K**(C-1))
	i += query_range_first*(q-1)
	if C<1 or q>S:
		return "IMPOSSIBLE"
	if q==K:
		print "YES!"
		return i+1
	return has_gold(K,C-1,S,i,q+1)

T = input()
for testcase in range(1,T+1):
	K,C,S = map(int, raw_input().split())
	print "\nINPUT: {},{},{}".format(K,C,S)
	result = has_gold(K,C,S,0,1)
	print "Case #{}: {}".format(testcase,result)
