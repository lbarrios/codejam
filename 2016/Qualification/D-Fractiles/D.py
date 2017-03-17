#!/usr/bin/env python
# -*- coding: utf-8 -*-
GOLD = "G"
LEAD = "L"

def has_gold(K,C,S):
	"""
	Returns true if we can answer if any of the originals K elements is gold
	given the C complexity, and the S graduate students
	"""
	return S*C >= K

def what_elements_to_query(K,C,S):
	element_to_query = 0
	queries = list()
	for s in range(1,S+1):
		element = 0
		for c in reversed(range(1,C+1)):
			sub_array_len = K**(c-1)
			element += (sub_array_len * element_to_query)
			element_to_query += 1
			if element_to_query >= K:
				queries.append(str(element + 1))
				return " ".join(queries)
		queries.append(str(element + 1))
	return " ".join(queries)
			

T = input()
for testcase in range(1,T+1):
	K,C,S = map(int, raw_input().split())
	#print "\nINPUT: {},{},{}".format(K,C,S)
	if not has_gold(K,C,S):
		result = "IMPOSSIBLE"
	else:
		result = what_elements_to_query(K,C,S)
		
	print "Case #{}: {}".format(testcase,result)
